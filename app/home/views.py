from django.shortcuts import render
import numpy as np
import pandas as pd

def HomePageView(request):
  df = pd.read_csv('templates/static/data/netflix.csv')
  data = {}
  data["dados"] = df.head().to_html(classes=['table','table-striped','mt-3'])
  return render (request, 'home/home.html', data)
