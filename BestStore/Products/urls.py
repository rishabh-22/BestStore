from django.urls import path
from .views import (
    cart_update, cart_empty, home, product_listings, ProductDetailView,
    cart_item_remove, FeaturedProduct, autocompletemodel,
    filter_listings)

urlpatterns = [
    path('', home, name="homepage"),
    path('products/', product_listings, name="products"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('api/product/cart/update/<int:pk>/', cart_update, name='cart-update'),
    path('api/product/cart/empty/', cart_empty, name='cart-empty-all'),
    path('api/product/cart/empty/<int:pk>/', cart_empty, name='cart-empty'),
    path('api/product/cart/remove/<int:pk>/', cart_item_remove, name='cart-item-remove'),
    path('featured/', FeaturedProduct.as_view(), name='featured'),
    path('ajax/search/', autocompletemodel, name='auto'),
    path('products/filter/', filter_listings, name='filter')
    #path('/newsletter/', newsletter, name='newsletter'),
]
