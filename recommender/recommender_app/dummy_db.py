from recommender_app.models import *
from random import randrange
from datetime import timedelta
from itertools import combinations
from time import sleep
import sys, math, random, datetime
import string
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def populate():
    brand_names = ['Nike', 'Adidas', 'Puma', 'Reebok', 'Alley Solly', 'Peter England', 'Louis Philippe', 'Abercrombie', 'Roadster', 'Max', 'FCUK', 'Provogue']
    clothing_types = ['Casual', 'Sports', 'Formal', 'Party']

    for brand in brand_names:
        for c_type in clothing_types:
            if not Brand.objects.filter(name=brand, clothing_type=c_type).exists():
                obj = Brand(name=brand, clothing_type=c_type)
                obj.save()
    brands = Brand.objects.all()
    colors = ['Black', 'White', 'Red', 'Green', 'Blue', 'Cyan', 'Megenta', 'Yellow', 'Pink', 'Navy Blue', 'Gray', 'Brown']
    garment_types = ['Upper', 'Lower']
    garment_sub_types = {'Upper' : ['Shirt', 'Tee', 'Jacket', 'Polo'],
                        'Lower' : ['Jeans', 'Chinos', 'Shorts', 'Tracks'] }

    sizes = {'Upper' : [36, 39, 40, 42, 44, 46, 48, 50],
             'Lower' : [26, 28, 30, 32, 34, 36, 38 , 40] }

    patterns = {'Upper' : ['Solid', 'Floral', 'Spotted', 'Checkered', 'Striped', 'Graphics'],
                'Lower' : ['Solid', 'Floral', 'Spotted', 'Checkered', 'Striped', 'Graphics'] }

    gender = ['Male', 'Female', 'Unisex']

    neckline = {'Upper' : ['Collar', 'V neck', 'Round', 'Banded'],
                'Lower' : ['NA'] }

    sleeves = {'Upper' : ['Short', 'Long'],
                'Lower' : ['NA'] }

    fits = {'Upper' : ['Slim', 'Custom', 'Regular', 'Sport'],
            'Lower' : ['Slim', 'Narrow', 'Custom', 'Regular', 'Tight'] }

    for i in range(100):
        print i+1
        l_color_idx_1 = random.randint(0, len(colors)-1)
        l_color_idx_2 = random.randint(0, len(colors)-1)
        while l_color_idx_1 == l_color_idx_2:
            l_color_idx_2 = random.randint(0, len(colors)-1)
        l_color_1 = colors[l_color_idx_1]
        l_color_2 = colors[l_color_idx_2]
        l_garment_type = garment_types[random.randint(0, len(garment_types)-1)]
        l_garment_sub_type = garment_sub_types[l_garment_type][random.randint(0, len(garment_sub_types[l_garment_type])-1)]
        l_pattern = patterns[l_garment_type][random.randint(0, len(patterns[l_garment_type])-1)]
        if l_pattern == 'Floral':
            l_gender = 'Female'
        else:
            l_gender = gender[random.randint(0,len(gender)-1)]
        l_neckline = neckline[l_garment_type][random.randint(0, len(neckline[l_garment_type])-1)]
        l_sleeves = sleeves[l_garment_type][random.randint(0, len(sleeves[l_garment_type])-1)]
        l_fit = fits[l_garment_type][random.randint(0, len(fits[l_garment_type])-1)]
        l_brand = brands[random.randint(0, len(brands)-1)]
        l_price = random.randint(700,2500)
        g_obj = Garment(name=l_brand.name+':'+l_brand.clothing_type+':'+l_pattern,
                        color_1=l_color_1, color_2=l_color_2, garment_type=l_garment_type,
                        garment_sub_type=l_garment_sub_type, pattern=l_pattern,
                        gender=l_gender, brand=l_brand, neckline=l_neckline,
                        sleeves=l_sleeves, fit=l_fit, price=l_price)
        g_obj.save()


def insert_users(n=105):
    print "Adding Users...",
    n+=1
    f = open("dummy_db/students.txt", "r+")
    stu_list = f.readlines()
    length = n-1
    for i,stu in enumerate(stu_list):
        n-=1;
        if n <= 0:
            break
        line = stu.split('$')
        username = line[0]
        password = line[1]
        first_name = line[2]
        last_name = line[3]
        address = line[4]
        email = line[5]
        phone_number = line[6]
        gender = line[7].rstrip('\n')
        if not User.objects.filter(name=first_name+last_name).exists():
            user_obj = User(name=first_name+last_name, email=email, phone_number=phone_number, gender=gender, birth_date = models.DateField())
            user_obj.save()
    f.close()
    print ""


def main():
    d1 = datetime.strptime('1/1/1974 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/1995 4:50 AM', '%m/%d/%Y %I:%M %p')

    print random_date(d1, d2)    
    user_obj = User(name=first_name+last_name, email=email, phone_number=phone_number, gender=gender, birth_date = random_date(d1, d2))
    user_obj.save()



if __name__ == "__main__":
    print "hrre"
    main()        