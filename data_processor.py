import pandas as pd 
import numpy as np


# Добавление библиотек PySpark

# Импорт необходимых модулей
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# Создание Spark сессии
spark = SparkSession.builder \
    .appName("PizzaRestaurantAnalysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

# Проверка
spark



