from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import lit

METERS_PER_FOOT = 0.3048
FEET_PER_MILE = 5280
EARTH_RADIUS_IN_METERS = 6371e3
METERS_PER_MILE = METERS_PER_FOOT * FEET_PER_MILE


def compute_distance(_spark: SparkSession, dataframe: DataFrame) -> DataFrame:
    dataframe.show()
    #dataframe.createOrReplaceTempView("citibike_data")
    #distance_df = _spark.sql("""select radians(end_station_latitude - start_station_latitude) as latitude_difference,
    #                         radians(end_station_longitude - start_station_longitude) as longitude_difference, *
    #                         from citibike_data""")
    return dataframe.withColumn("distance", lit(0.0))


def run(spark: SparkSession, input_dataset_path: str, transformed_dataset_path: str) -> None:
    input_dataset = spark.read.parquet(input_dataset_path)
    input_dataset.show()

    dataset_with_distances = compute_distance(spark, input_dataset)
    dataset_with_distances.show()

    dataset_with_distances.write.parquet(transformed_dataset_path, mode='append')
