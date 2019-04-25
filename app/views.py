import numpy as np
from sklearn.externals import joblib
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import status
from rest_framework.decorators import action

from .models import Iris
from .serializer import IrisSerializer
from django.conf import settings

PKL_PATH = f'{settings.BASE_DIR}/static/clf/iris.pkl'


class IrisViewSet(viewsets.ModelViewSet):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer

    @list_route(methods=['post'])
    def detection(self, request):

        data = request.data.copy()
        sepal_length = data["sepal_length"]
        sepal_width = data["sepal_width"]
        petal_length = data["petal_length"]
        petal_width = data["petal_width"]

        clf = joblib.load(PKL_PATH)
        score = clf.predict(
            np.array([
                [sepal_length, sepal_width, petal_length, petal_width]
            ])
        )
        data["score"] = score[0]

        serializer = IrisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        label = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        data['label'] = label[data['score']]
        return Response(data, status=status.HTTP_200_OK)
