import asyncio
import logging
import sys
import json
import requests
import datetime
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import (
    Command,
    CommandObject,
    ExceptionMessageFilter,
    ExceptionTypeFilter,
)
# envs from .env file
from data import config

# Initialize Bot instance with a default parse mode which will be passed to all API calls
# And the run events dispatching
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
