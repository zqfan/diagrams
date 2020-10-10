# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _TencentCloud


class _Database(_TencentCloud):
    _type = "database"
    _icon_dir = "resources/tencentcloud/database"


class DataTransmissionService(_Database):
    _icon = "data-transmission-service.png"


class Tdata(_Database):
    _icon = "tdata.png"


class TencentDbCtsdb(_Database):
    _icon = "tencent-db-ctsdb.png"


class TencentDbCynosdb(_Database):
    _icon = "tencent-db-cynosdb.png"


class TencentDbMariadb(_Database):
    _icon = "tencent-db-mariadb.png"


class TencentDbMemcached(_Database):
    _icon = "tencent-db-memcached.png"


class TencentDbMongodb(_Database):
    _icon = "tencent-db-mongodb.png"


class TencentDbMysql(_Database):
    _icon = "tencent-db-mysql.png"


class TencentDbPostgresql(_Database):
    _icon = "tencent-db-postgresql.png"


class TencentDbRedis(_Database):
    _icon = "tencent-db-redis.png"


class TencentDbSqlserver(_Database):
    _icon = "tencent-db-sqlserver.png"


class TencentDbTcaplusdb(_Database):
    _icon = "tencent-db-tcaplusdb.png"


class TencentDbTdsql(_Database):
    _icon = "tencent-db-tdsql.png"


# Aliases

CDB = TencentDbMysql
TDSQL = TencentDbTdsql
CTSDB = TencentDbCtsdb
CynosDB = TencentDbCynosdb
TData = Tdata
TcaplusDB = TencentDbTcaplusdb
MariaDB = TencentDbMariadb
Redis = TencentDbRedis
DTS = DataTransmissionService
SQLServer = TencentDbSqlserver
MongoDB = TencentDbMongodb
PostgreSQL = TencentDbPostgresql
Memcached = TencentDbMemcached
