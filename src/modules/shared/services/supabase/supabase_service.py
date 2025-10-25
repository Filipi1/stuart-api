from typing import Any, Dict, List, Optional

from supabase import AsyncClient, AsyncClientOptions, acreate_client


class SupabaseService:
    def __init__(self, url: str, key: str, schema: str = "public") -> None:
        self.__url = url
        self.__key = key
        self.__schema = schema
        self.supabase: Optional[AsyncClient] = None

    async def create_client(self) -> AsyncClient:
        if self.supabase is not None:
            return self.supabase

        self.supabase = await acreate_client(
            self.__url, self.__key, options=AsyncClientOptions(schema=self.__schema)
        )
        return self.supabase

    async def create(self, table: str, data: dict) -> dict:
        self.supabase = await self.create_client()
        response = await self.supabase.table(table).insert(data).execute()
        return response.data[0]

    async def read(self, table: str, where: dict) -> list[dict]:
        self.supabase = await self.create_client()

        response = self.supabase.table(table).select("*")
        for key, value in where.items():
            response = response.eq(key, value)
        response = await response.execute()
        return response.data

    async def update(self, table: str, id: str, data: dict) -> List[Dict[str, Any]]:
        self.supabase = await self.create_client()
        await self.supabase.table(table).update(data).eq("id", int(id)).execute()
        updated_data = await self.read(table, {"id": int(id)})
        return updated_data

    async def delete(self, table: str, id: str) -> Optional[Dict[str, Any]]:
        self.supabase = await self.create_client()
        response = await self.supabase.table(table).delete().eq("id", id).execute()
        return response.data[0] if len(response.data) > 0 else None

    async def upload_file(self, filename: str, file: bytes) -> str:
        self.supabase = await self.create_client()
        storage = "memes-staging" if self.__schema == "staging" else "memes"
        response = await self.supabase.storage.from_(storage).upload(filename, file)
        return response.path

    def get_storage_url(self, filename: str) -> str:
        storage = "memes-staging" if self.__schema == "staging" else "memes"
        return f"{self.__url}/storage/v1/object/public/{storage}/{filename}"

    async def custom_query(
        self,
        main_table: str,
        select_fields: List[str],
        where_conditions: Optional[Dict[str, Any]] = None,
        order_by: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        self.supabase = await self.create_client()

        select_query = ",".join(select_fields)
        query = self.supabase.table(main_table).select(select_query)

        if where_conditions:
            for key, value in where_conditions.items():
                if isinstance(value, dict):
                    for operator, operator_value in value.items():
                        if operator == "gte":
                            query = query.gte(key, operator_value)
                        elif operator == "lte":
                            query = query.lte(key, operator_value)
                        elif operator == "gt":
                            query = query.gt(key, operator_value)
                        elif operator == "lt":
                            query = query.lt(key, operator_value)
                        elif operator == "neq":
                            query = query.neq(key, operator_value)
                        elif operator == "in":
                            query = query.in_(key, operator_value)
                else:
                    query = query.eq(key, value)

        if order_by:
            for field, direction in order_by.items():
                query = query.order(field, desc=(direction.lower() == "desc"))

        if limit:
            query = query.limit(limit)

        if offset:
            query = query.range(offset, offset + (limit or 0) - 1)

        response = await query.execute()
        return response.data
