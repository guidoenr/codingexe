import boto3
"""
Refactor the next function using yield to return the array of objects found by the
`s3.list_objects_v2` function that matches the given prefix.
"""
def get_s3_objects(bucket, prefix=''):
    s3 = boto3.client('s3')

    kwargs = {'Bucket': bucket}
    next_token = None
    if prefix:
        kwargs['Prefix'] = prefix
    
    while True:
        if next_token:
            kwargs['ContinuationToken'] = next_token
        resp = s3.list_objects_v2(**kwargs)
        contents = resp.get('Contents', [])
        for obj in contents:
            key = obj['Key']
            if key.startswith(prefix):
                yield obj
        next_token = kwargs.get('NextContinuationToken', None)
        if not next_token:
            break
"""
@guidoenr
now, you can use the generator instead of the complete list

s3_objects = get_s3_objects(...)
print(next(s3_objects) 

or whatever you want to do it with the new refactorized function
"""

"""
Please, explain and document iterations, conditionals, and the
function as a whole
"""
def fn(main_plan, obj, str_id, pm, extensions=[]):
    
    items = []
    sp = False
    cd = False

    ext_p = {}

    """@guidoenr
    watching this part of the function, i noticed that
    the ext_p is a dictionary like

    ext_p = {
        'price': PriceObject
        'qty': int  #quantity
    }

    and the Price is a Class, because in the function below
    there is an access to one of his attributes
    ['price'].id

    class Price:
        def __init__(self, id):
            self.id = id

    also, watching below in the code, i realized
    that the 'qty' is the quantity of the item
    and in the ext_p dictionary is indexed
    by the item.price.id, so, its like a kind off 
    'STOCK' dictionary  ext_p = {price_id, quantity}

    """
    for ext in extensions:
        ext_p[ext['price'].id] = ext['qty']

    """@guidoenr
    the obj is another dictionary
    containing also Objects...
    and the data field, might be a list,
    something like:

    obj_dict = {
        'items' : Object
    }

    class Obj:
        def __init__(self, data_list):
            self.data = data_list # where this data attr is a List of Items

    there is another class called maybe 'Item'

    class Item:
        def __init__(self, id, price):
            self.id = id
            self.price = price # PriceObject

    """
    for item in obj['items'].data:
        product = {
            'id': item.id
        }

        """@guidoenr
        here, if the item price's id is not in the "main_plan" what is like
        a kind off class that envolves a customer plan to buy items
        and the ext_p looks like a 'stock' dictionary
        because this conditional is comparing if that price id is not
        in the ext_p
        """
        if item.price.id != main_plan.id and item.price.id not in ext_p:
            product['deleted'] = True
            cd = True
            """@guidoenr
            this section it's a quite easy to think, because
            the elif conditional, check if we have stock 
            of the item in the ext_p (STOCK) dictionary
            and if that item (item price's id) exists in the 
            dictionary, then, and if statement check if 
            we have quantity of that item in order to be
            putted in the dictionary of the boughted product
            'deleted' or the quantity
            """
        elif item.price.id in ext_p:
            qty = ext_p[item.price.id]
            if qty < 1: # if there is not stock of the product (qty=0), the product is deleted
                product['deleted'] = True
            else:
                """@guidoenr
                and, if there is stock in the ext_p dict
                we put all the quantity of the item
                in the product dict (thats a kind of weird)
                """
                product['qty'] = qty
            # then, the item will be deleted from the stock
            del ext_p[item.price.id]
        elif item.price.id == main_plan.id:
            sp = True

        items.append(product)
    
    """@guidoenr
    the sp boolean works like a kind of 'some products' variable
    because, when the sp gets the False value, there's only 
    one quantity of the item, and it's the basic main plan
    """
    if not sp:
        items.append({
            'price': main_plan.id,
            'quantity': 1
        })
    """@guidoenr
    and here, we iterate over all the items of the ext_p
    dictionary and we add all the price and the quantity
    of the required items
    """
    for price, qty in ext_p.items():
        if qty < 1:     # ?
            continue
        items.append({
            'price': price,
            'quantity': qty
        })
    
    """@guidoenr
    the pm arg is the payment method, also an Object
    with his attributes like id
    """
    kwargs = {
        'items': items,
        'default_payment_method': pm.id,
        'api_key': API_KEY,
    }
    
    return items

    """@guidoenr
    In summary, the function is basically a kind of 
    product purchase operation, where there is also 
    a dictionary that acts as a stock, where (strangely) 
    a purchase can be of the main plan, or of the whole 
    quantity of a product.
    there are also several attributes that are not used, 
    such as the dictionary kwargs, the boolean cd, among 
    others.
    """

"""
Having the class `Caller` and the function `fn`
Refactor the function `fn` to execute any method from `Caller` using the argument `fn_to_call`
reducing the `fn` function to only one line.
"""
class Caller():
    add = lambda a, b : a + b
    concat = lambda a, b : f'{a},{b}'
    divide = lambda a, b : a / b
    multiply = lambda a, b : a * b

def fn(fn_to_call, *args):
    """@guidoenr
    with the function 'getattr' i can return any atribute of any class
    and, in this case, the 'fn_to_call' have the same name of the 
    lambda attribute of the class Caller
    """
    return None if fn_to_call == None else getattr(Caller, fn_to_call)(*args);

    
"""
A video transcoder was implemented with different presets to process different videos in the application. The videos should be
encoded with a given configuration done by this function. Can you explain what this function is detecting from the params
and returning based in its conditionals?
"""
def fn(config, w, h):
    """@guidoenr
    basically what this function does is to resize or find the best 
    resolution for you based on your width, height and aspect ratio. 
    (corresponding to the video resolution)
    so, you have 3 dictionaries that correspond to the orientations 
    of an image, where each dictionary has several resolutions, something
    like 1280x920, 800x600, etc

    's' -> square
    'p' -> portrait
    'l' -> landscape 

    then, the 3 if statements only check that the aspect ratio is 
    within the range that corresponds to each of the orientations, 
    then, it searches in the dictionaries for the resolutions that best 
    matches the input resolution, based on the width being smaller.
    """
    v = None
    ar = w / h #aspect-ratio

    if ar < 1:
        v = [r for r in config['p'] if r['width'] <= w]
    elif ar > 4 / 3:
        v = [r for r in config['l'] if r['width'] <= w]
    else:
        v = [r for r in config['s'] if r['width'] <= w]

    return v


"""
Having the next helper, please implement a refactor to perform the API call using one method instead of rewriting the code
in the other methods.
"""
import requests
class Helper:
    DOMAIN = 'http://example.com'
    SEARCH_IMAGES_ENDPOINT = 'search/images'
    GET_IMAGE_ENDPOINT = 'image'
    DOWNLOAD_IMAGE_ENDPOINT = 'downloads/images'

    AUTHORIZATION_TOKEN = {
        'access_token': None,
        'token_type': None,
        'expires_in': 0,
        'refresh_token': None
    }

    """@guidoenr
    i made the make_request method, receiving the uri as a param
    and the method of the REST VERB, because there are the only 
    values that could be different from each request, (not including the **kwargs)
    so, thats all.. all the tokens are the same in each request
    """
    def make_request(self, uri, method, **kwargs):
        token_type = self.AUTHORIZATION_TOKEN['token_type']
        access_token = self.AUTHORIZATION_TOKEN['access_token']

        headers = {
            'Authorization': f'{token_type} {access_token}',
        }

        URL = f'{self.DOMAIN}/{uri}'
        
        send = {
            'headers': headers,
            'params': kwargs
        }
        response = requests.request(method, URL, **send)
        return response

        
    def search_images(self, **kwargs):
        '''@guidoenr
        first, i have the thought of make the proccess
        of complete the uri in the make_request method as well,
        but there's gonna be 3 if statements, and the time complexity
        gonna be the same, so, i opted for this solution.
        '''
        uri = self.SEARCH_IMAGES_ENDPOINT
        self.make_request(uri, 'GET', **kwargs)

        
    def get_image(self, image_id, **kwargs):
        uri = f'{self.GET_IMAGE_ENDPOINT}/{image_id}'
        self.make_request(uri, 'GET', **kwargs)


    def download_image(self, image_id, **kwargs):
        uri = f'{self.DOWNLOAD_IMAGE_ENDPOINT}/{image_id}'
        self.make_request(uri, 'POST', **kwargs)
