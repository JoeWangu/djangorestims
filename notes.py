# SERIALIZER NOTES
# The serializer is used to convert the data into a format that can be sent over the network.
#examples from serializer.py in inventory

# to include all fields at once
# class FamilySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Family
#         fields = '__all__'

# to exclude some fields
# class FamilySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Family 
#         exclude = 'minQuantity'

# in class ProductSerializer....As you can see we have included the related models location and family .In this case ModelSerializer takes the primary keys by default so you'll get something like this, depending on data you have in your database. ..."location": 1,...
# What if you want to get the whole related objects ?
# You can use the depth option in Meta class eg.
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product 
#         fields = ('sku','barcode', 'title', 'description','location','family')
#         depth = 1
# you will get something like this,
# {
#         "sku": "Product001",
#         "barcode": "xxxxxxxxx",
#         "title": "Product 001",
#         "description": "product 001",
#         "location": {
#             "id": 1,
#             "reference": "LOC001",
#             "title": "Location 001",
#             "description": "Location 001"
#         },
# Or you can specify the fields explicitly .
# class ProductSerializer(serializers.ModelSerializer):

#     location = LocationSerializer()
#     family = FamilySerializer()
#     class Meta:
#         model = Product 
#         fields = ('sku','barcode', 'title', 'description','location','family')

# Using ModelSerializer ,the default way to serialize a relationship field is primary keys but we have also other representations such as :
# 1.Hyperlinks - uses hyperlinks instead of primary keys to represent relationships .
# 2.Complete nested instances ,
# 3.Custom representation