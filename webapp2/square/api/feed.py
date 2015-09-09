from square.serializers import SquareSerializer

def square_of_user_feed(user):
    serializer = SquareSerializer(user.square_set.filter(active=True), many=True)
    data = serializer.data
    return {'square_of_user_feed': data}

def delivery_square_of_user_feed(user):
    serializer = SquareSerializer(user.deliverysquare.all().values('id'), many=True)
    data = serializer.data
    return {'delivery_square_of_user_feed': data}