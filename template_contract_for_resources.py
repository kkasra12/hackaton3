import smartpy as sp


@sp.module
def main():
    class Resource(sp.Contract):
        def __init__(
            self,
            item_name,
            city,
            unit,
            price,
            availablity,
            technical_compliance,
            carbon_footprint,
            id,
        ):
            self.data.item_name = item_name
            self.data.city = city
            self.data.unit = unit
            self.data.price = price
            self.data.availablity = availablity
            self.data.technical_compliance = technical_compliance
            self.data.carbon_footprint = carbon_footprint
            self.data.id = id

        # setters
        @sp.entrypoint
        def set_price(self, new_price):
            assert new_price >= 0, "price must be positive"
            self.data.price = new_price

        @sp.entrypoint
        def set_availability(self, new_availability):
            assert (
                0 <= new_availability and new_availability <= 2
            ), "availability must be between 0 and 2"
            self.data.availablity = new_availability

        @sp.entrypoint
        def set_technical_compliance(self, new_technical_compliance):
            self.data.technical_compliance = new_technical_compliance

        @sp.entrypoint
        def set_carbon_footprint(self, new_carbon_footprint):
            assert new_carbon_footprint >= 0, "carbon footprint must be positive"
            self.data.carbon_footprint = new_carbon_footprint

        # getters
        # @sp.entrypoint
        # def get_item_name(self):
        #     sp.result(self.data.item_name)

        # @sp.entrypoint
        # def get_city(self):
        #     sp.result(self.data.city)

        # @sp.entrypoint
        # def get_unit(self):
        #     sp.result(self.data.unit)

        # @sp.entrypoint
        # def get_price(self):
        #     sp.result(self.data.price)

        # @sp.entrypoint
        # def get_availability(self):
        #     sp.result(self.data.availablity)

        # @sp.entrypoint
        # def get_technical_compliance(self):
        #     sp.result(self.data.technical_compliance)

        # @sp.entrypoint
        # def get_carbon_footprint(self):
        #     sp.result(self.data.carbon_footprint)


@sp.add_test()
def test():
    # We define a test scenario, together with some outputs and checks
    # The scenario takes the module as a parameter
    scenario = sp.test_scenario("Dummy", main)

    c1 = main.Resource(
        "item_name",
        "city",
        "unit",
        100,
        1,
        "technical_compliance",
        "carbon_footprint",
        1,
    )
    scenario += c1
