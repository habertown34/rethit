from web3 import Web3

def init():
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

    # open abi file
    abi_file = open('c:/dev/py/web3/build/rethit-abi.json')
    abi = abi_file.read()
    abi_file.close()

    # paste contract address here
    contract_address = '0x6533D418b7B82696006493cE8380d830009befeF'

    # create instance
    instance = web3.eth.contract(
        address=contract_address,
        abi=abi
    )

    # set account
    web3.eth.defaultAccount = web3.eth.accounts[0]

    return web3, instance

def get_basic():
    web3, instance = init()
    return web3.eth.defaultAccount, instance.address

def get_balance():
    web3 = init()[0]
    return web3.eth.getBalance(web3.eth.defaultAccount) / 1000000000000000000

def create_post(message):
    instance = init()[1]
    instance.functions.create(message).transact()

def upvote(post_id):
    instance = init()[1]
    instance.functions.upvote(post_id).transact()
    return get_post(post_id)['votes']

def downvote(post_id):
    instance = init()[1]
    instance.functions.downvote(post_id).transact()
    return get_post(post_id)['votes']

def get_post(post_id):
    instance = init()[1]
    post = instance.functions.posts(post_id).call()
    post_dict = {}
    post_dict['id'] = post[0]
    post_dict['sender'] = post[1]
    post_dict['message'] = post[2]
    post_dict['votes'] = post[3]
    return post_dict

def get_number_of_posts():
    instance = init()[1]
    return instance.functions.latestPostID().call()

def get_all_posts():
    posts = []
    i = get_number_of_posts()
    for n in range(1, i + 1):
        posts.append(get_post(n))
    return posts