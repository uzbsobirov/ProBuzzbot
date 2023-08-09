from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        user_id BIGINT NOT NULL UNIQUE,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_sponsor(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Sponsor (
        id SERIAL PRIMARY KEY,
        chat_id BigInt NOT NULL UNIQUE,
        chat_title TEXT,
        chat_type VARCHAR(10),
        chat_link TEXT,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_cards(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Cards (
        id SERIAL PRIMARY KEY,
        number TEXT UNIQUE,
        callback_data TEXT,
        name TEXT,
        owner_name TEXT,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_categories(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Category (
        id SERIAL PRIMARY KEY UNIQUE,
        name TEXT,
        call_data TEXT UNIQUE,
        child BigInt NULL,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_child_category(self):
        sql = """
        CREATE TABLE IF NOT EXISTS ChildCategory (
        id SERIAL PRIMARY KEY UNIQUE,
        name TEXT,
        call_data TEXT UNIQUE,
        related_id BigInt,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_inner_category(self):
        sql = """
        CREATE TABLE IF NOT EXISTS InnerCategory (
        id SERIAL PRIMARY KEY UNIQUE,
        name TEXT,
        call_data TEXT UNIQUE,
        order_id BigInt,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_orders(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Orders (
        id SERIAL PRIMARY KEY UNIQUE,
        order_id BigInt UNIQUE,
        name TEXT,
        call_data TEXT UNIQUE,
        price BigInt,
        description TEXT,
        date_joined DATE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name: str, username: str, user_id: int, date_joined: str):
        sql = "INSERT INTO users (full_name, username, user_id, date_joined) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, full_name, username, user_id, date_joined, fetchrow=True)

    async def add_sponsor(self, chat_id: str, chat_title: str, chat_type: int, chat_link: str, date_joined):
        sql = "INSERT INTO Sponsor (chat_id, chat_title, chat_type, chat_link, date_joined) " \
              "VALUES($1, $2, $3, $4, $5) returning *"
        return await self.execute(sql, chat_id, chat_title, chat_type, chat_link, date_joined, fetchrow=True)

    async def add_card(self, number: str, callback_data: str, name: int, owner_name: str, date_joined):
        sql = "INSERT INTO Cards (number, callback_data, name, owner_name, date_joined) " \
              "VALUES($1, $2, $3, $4, $5) returning *"
        return await self.execute(sql, number, callback_data, name, owner_name, date_joined, fetchrow=True)

    async def add_category(self, name: str, call_data: str, child: int, date_joined):
        sql = "INSERT INTO Category (name, call_data, child, date_joined) " \
              "VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, name, call_data, child, date_joined, fetchrow=True)

    async def add_child_category(self, name: str, call_data: str, related_id: int, date_joined):
        sql = "INSERT INTO ChildCategory (name, call_data, related_id, date_joined) " \
              "VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, name, call_data, related_id, date_joined, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_sponsor(self):
        sql = "SELECT * FROM Sponsor"
        return await self.execute(sql, fetch=True)

    async def select_all_category(self):
        sql = "SELECT * FROM Category"
        return await self.execute(sql, fetch=True)

    async def select_all_childcategory(self):
        sql = "SELECT * FROM ChildCategory"
        return await self.execute(sql, fetch=True)

    async def select_all_cards(self):
        sql = "SELECT * FROM Cards"
        return await self.execute(sql, fetch=True)

    async def select_one_users(self, user_id):
        sql = "SELECT * FROM Users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetch=True)

    async def select_one_category(self, call_data):
        sql = "SELECT * FROM Category WHERE call_data=$1"
        return await self.execute(sql, call_data, fetch=True)

    async def select_one_child_category(self, call_data):
        sql = "SELECT * FROM ChildCategory WHERE call_data=$1"
        return await self.execute(sql, call_data, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_issubs(self, issubs, user_id):
        sql = "UPDATE Users SET issubs=$1 WHERE user_id=$2"
        return await self.execute(sql, issubs, user_id, execute=True)

    async def update_category_name(self, name, call_data):
        sql = "UPDATE Category SET name=$1 WHERE call_data=$2"
        return await self.execute(sql, name, call_data, execute=True)

    async def delete_sponsor(self, chat_id):
        sql = "DELETE FROM Sponsor WHERE chat_id=$1"
        await self.execute(sql, chat_id, execute=True)

    async def delete_one_category(self, call_data):
        sql = "DELETE FROM Category WHERE call_data=$1"
        await self.execute(sql, call_data, execute=True)

    async def drop_courses(self):
        await self.execute("DROP TABLE Courses", execute=True)
