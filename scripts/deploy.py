from brownie import accounts, network, config, SimpleContract


def deploy_simple_contract(isFirst=True):
    current_account = get_account()
    simple_contract_obj = get_contract(current_account)
    heroes = simple_contract_obj.getAllHeroes()
    print("0", heroes)
    if isFirst:
        add_obi_wan_kenobi_txn = simple_contract_obj.addHero(
            "Obi-Wan Kenobi", "Blue", 29, {"from": current_account}
        )
        add_obi_wan_kenobi_txn.wait(1)
        add_darth_vader_txn = simple_contract_obj.addHero(
            "Darth Vader", "Red", 60, {"from": current_account}
        )
        add_darth_vader_txn.wait(1)

    heroes = simple_contract_obj.getAllHeroes()
    print("1:", heroes)

    return simple_contract_obj


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_by_name(simple_contract_obj, name):
    return simple_contract_obj.getHeroByName(name)


def get_contract(current_account):
    try:
        simple_contract_obj = SimpleContract[-1]
        return simple_contract_obj
    except:
        simple_contract_obj = SimpleContract.deploy({"from": current_account})
        return simple_contract_obj


def main():
    simple_contract_obj = deploy_simple_contract()
    name = input("Please enter a hero name:")
    print(get_by_name(simple_contract_obj, name))
