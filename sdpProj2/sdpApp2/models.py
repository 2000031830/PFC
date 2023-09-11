from django.db import models

COUNTRY = [
("Afghanistan",'Afghanistan'),
("Armenia",'Armenia'),
("Azerbaijan"   ,'Azerbaijan'),
("Bahrain"   ,'Bahrain'),
("Bangladesh"   ,'Bangladesh'),
("Bhutan"   ,'Bhutan'),
("Brunei"   ,'Brunei'),
("Cambodia"   ,'Cambodia'),
("China"   ,'China'),
("Georgia"   ,'Georgia'),
("Hong Kong SAR China",'Hong Kong SAR China'),
 ("India"   ,'India'),
("Indonesia"   ,'Indonesia '),
("Iran"   ,'Iran '),
 ("Iraq"   ,'Iraq '),
("Israel"   ,'Israel'),
   ("Japan"   ,'Japan'),
   ("Jordan"   ,'Jordan'),
   ("Kazakhstan"   ,'Kazakhstan'),
   ("Kuwait"   ,'Kuwait'),
   ("Kyrgyzstan"   ,'Kyrgyzstan' ),
   ("Laos"   ,'Laos'),
   ("Lebanon"   ,'Lebanon'),
   ("Macau SAR China"   ,'Macau SAR China' ),
   ("Malaysia"   ,'Malaysia'),
   ("Maldives"   ,'Maldives'),
   ("Mongolia"   ,'Mongolia' ),
   ("Myanmar"   ,'Myanmar'),
   ("Nepal"   ,'Nepal'),
   ("Neutral Zone"   ,'Neutral Zone'),
   ("North Korea"   ,'North Korea'),
   ("Oman"   ,'Oman'),
   ("Pakistan"   ,'Pakistan'),
   ("Palestinian Territories"   ,'Palestinian Territories'),
   ("People's Democratic Republic of Yemen"   ,'Peoples Democratic Republic of Yemen'),
   ("Philippines"   ,'Philippines'),
   ("Qatar"   ,'Qatar'),
   ("Saudi Arabia"   ,'Saudi Arabia'),
   ("Singapore"   ,'Singapore'),
   ("South Korea"   ,'South Korea'),
   ("Sri Lanka"   ,'Sri Lanka'),
   ("Syria"   ,'Syria'),
   ("Taiwan"   ,'Taiwan'),
   ("Tajikistan"   ,'Tajikistan'),
   ("Thailand"   ,'Thailand'),
   ("Timor-Leste"   ,'Timor-Leste'),
   ("Turkey"   ,'Turkey'),
   ("Turkmenistan"   ,'Turkmenistan '),
   ("United Arab Emirates"   ,'United Arab Emirates'),
   ("Uzbekistan",'Uzbekistan'),
    ("Vietnam",'Vietnam'),
    ("Yemen",'Yemen')

]

SHIPMENT_MODE =[
    ("Ship",'Ship'),
    ("Bus",'Bus'),
    ("Train",'Train'),
    ("Plane",'Plane')
]


class Porders(models.Model):
    objects = None
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    orderquantity = models.IntegerField()
    country = models.CharField(max_length=100,choices=COUNTRY)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=100)
    shipmentmode = models.CharField(max_length=100,choices=SHIPMENT_MODE)
    def __int__(self):
        return self.orderquantity

