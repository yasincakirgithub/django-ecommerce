from faker import Faker
from blog.models import Blog,Category,Tags
from users.models import CustomUserModel
from products.models import ProductImage,ProductCategory,ProductSize,Product
import random
import string

fake = Faker()

def add_user(amount):
    for i in range(0,amount):
        created_user = CustomUserModel.objects.create(
            email = fake.email(),
            first_name = fake.first_name(),
            last_name = fake.last_name()
        )
        print("Added ",i)

def add_blog_category(amount):
    for i in range(0,amount):
        created_category,created = Category.objects.get_or_create(
            name= fake.sentence(nb_words=1).replace(".","")
        )
        print("Added ",i)

def add_blog_tag(amount):
    for i in range(0,amount):
        created_tag,created = Tags.objects.get_or_create(
            name= fake.sentence(nb_words=1).replace(".","")
        )
        print("Added ",i) 

def add_blog(amount):
    #from scripts.add_dummy_data import add_blog;add_blog(100)
    for i in range(0,amount):

        blog_obj = Blog.objects.create(
            title = fake.sentence(nb_words=1).replace(".",""),
            text = fake.text(max_nb_chars=2000),
            image = "blog/pngtree-two-sides-of-a-tree-in-the-desert-image_2873370.jpg",
            category = Category.objects.order_by("?").first(),
            created_by = CustomUserModel.objects.order_by("?").first(),
        )
        blog_obj.tags.add(*Tags.objects.order_by("?")[0:4])
        print("Added ",i)

def add_product(amount):
    #from scripts.add_dummy_data import add_product;add_product(100)
    for i in range(0,amount):

        product_obj = Product.objects.create(
            name = fake.sentence(),
            price = round(random.uniform(1, 100),2),
            currency = random.choice(["$","€"]),
            description = fake.text(max_nb_chars=200),
            additional_information = fake.text(max_nb_chars=100),
            code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)),
            category =  ProductCategory.objects.order_by("?").first()
        )
        product_obj.images.add(*ProductImage.objects.order_by("?")[0:3])
        print("Added ",i)


        