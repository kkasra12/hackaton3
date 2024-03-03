raise NotImplementedError(
    "Please fill in the config_template.py and rename it to config.py"
)
db_config = {
    "dbname": "DBNAME",
    "user": "USERNAME",
    "password": "PASSWORD",
    "host": "HOSTNAME",
    "port": "5432",  # normally it is 5432 since we are using postgres
}

tezos_config = {
    "encoded_key": "ENCODED_KEY",
    "shell_addr": "https://ghostnet.tezos.marigold.dev",  # or any other shell address
}
