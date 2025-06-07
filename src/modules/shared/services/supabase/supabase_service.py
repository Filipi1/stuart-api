from supabase import AsyncClient, AsyncClientOptions
from typing import List, Dict, Any, Optional


class SupabaseService:
    def __init__(self, url: str, key: str, schema: str = "public") -> None:
        self.supabase = AsyncClient(url, key, options=AsyncClientOptions(schema=schema))

    async def create(self, table: str, data: dict) -> dict:
        response = await self.supabase.table(table).insert(data).execute()
        return response.data

    async def read(self, table: str, where: dict) -> list[dict]:
        response = self.supabase.table(table).select("*")
        for key, value in where.items():
            response = response.eq(key, value)
        response = await response.execute()
        return response.data

    async def update(self, table: str, id: str, data: dict) -> dict:
        response = await self.supabase.table(table).update(data).eq("id", id).execute()
        return response.data

    async def delete(self, table: str, id: str) -> dict:
        response = await self.supabase.table(table).delete().eq("id", id).execute()
        return response.data

    async def custom_query(
        self,
        main_table: str,
        select_fields: List[str],
        where_conditions: Optional[Dict[str, Any]] = None,
        order_by: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Executa uma query personalizada.
        
        Args:
            main_table: Nome da tabela principal
            select_fields: Lista de campos a serem selecionados
            where_conditions: Condições WHERE (opcional)
            order_by: Ordenação (opcional) - Exemplo: {"created_at": "desc"}
            limit: Limite de resultados (opcional)
        
        Returns:
            Lista de resultados da query
        """
        # Construir a query de seleção
        select_query = ",".join(select_fields)
        query = self.supabase.table(main_table).select(select_query)
        
        # Adiciona condições WHERE
        if where_conditions:
            for key, value in where_conditions.items():
                query = query.eq(key, value)
        
        # Adiciona ordenação
        if order_by:
            for field, direction in order_by.items():
                query = query.order(field, desc=(direction.lower() == "desc"))
        
        # Adiciona limite
        if limit:
            query = query.limit(limit)
        
        response = await query.execute()
        return response.data