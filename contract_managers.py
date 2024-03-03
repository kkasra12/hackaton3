from pytezos import ContractInterface
from pytezos import pytezos
from pytezos.crypto.key import Key
from pytezos.operation.result import OperationResult
from config import tezos_config


class contract_manager:
    def __init__(self, contract_file):
        sk = Key.from_encoded_key(tezos_config["encoded_key"])
        self.pytezos_ = pytezos.using(key=sk, shell=tezos_config["shell_addr"])
        self.resource = ContractInterface.from_file(contract_file)

    def send_contract(self, params: dict[str, any], verbose: int = 0) -> str:
        opg = self.pytezos_.bulk(self.resource.originate()).send(min_confirmations=2)
        ctr = [
            res.originated_contracts[0]
            for res in OperationResult.from_operation_group(opg.opg_result)
        ]
        if len(ctr) == 0:
            return "Failed to originate contract"
        elif len(ctr) > 1:
            print("Warning: There is several contracts:", *ctr, sep="\n")

        if verbose:
            print(ctr[0])
        resource = self.pytezos_.contract(ctr[0])
        for key, value in params.items():
            if verbose:
                print(f"setting {key} to {value}")
            resource.__getattribute__(f"set_{key}")(value).send(min_confirmations=2)
            # if key == "availability":
            #     resource.set_availability(value).send(min_confirmations=2)
            # elif key == "carbon_footprint":
            #     resource.set_carbon_footprint(value).send(min_confirmations=2)
            # elif key == "technical_compliance":
            #     resource.set_technical_compliance(value).send(min_confirmations=2)
            # elif key == "price":
            #     resource.set_price(value).send(min_confirmations=2)

        return ctr[0]

    def get_contract(self, contract_address: str) -> ContractInterface:
        if not contract_address.startswith("KT"):
            raise ValueError(
                "Invalid contract address, contract address must start with KT"
            )

        return pytezos.contract(contract_address)


if __name__ == "__main__":
    cm = contract_manager("resource_contract.tz")
    contract_addr = cm.send_contract(
        {
            "availability": 2,
            "carbon_footprint": 200,
            "technical_compliance": str(
                {"certification": "ISO 9001", "compliance": "EU"}
            ),
            "price": 1000,
        },
        verbose=1,
    )
    print(contract_addr)
    print(cm.get_contract(contract_addr))
