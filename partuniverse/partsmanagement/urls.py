# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView


from .views import *

urlpatterns = [
    # Some general url pattern
    url(r'^$',
        RedirectView.as_view(
            url='list',
            permanent=True),
        name='index'),
    url(r'^list/', PartsList.as_view(), name='part_list'),
    url(r'^rest/list/$', RestPartList.as_view()),
    url(r'^rest/(?P<pk>[0-9]+)/$', RestPartDetail.as_view()),
    url(r'^add/', login_required(PartsAddView.as_view()),
        name='part_add'),
    url(r'^reorderlist/$', PartsReorderList.as_view(),
        name='part_reorderlist'),
    # item specific ones
    url(r'^(?P<pk>[\w]+)/$', PartDetailView.as_view(),
        name='part_detail'),
    url(r'^(?P<pk>[\w]+)/delete/$',
        login_required(PartDeleteView.as_view()),
        name='part_delete'),
    url(r'^(?P<pk>[\w]+)/update/$',
        login_required(PartUpdateView.as_view()),
        name='part_update'),
    # Category
    url(r'^category/list', CategoryList.as_view(), name='category_list'),
    url(r'^category/add', CategoryAddView.as_view(), name='category_add'),
    url(r'^category/rest/list/$', RestCategoryList.as_view()),
    url(r'^category/rest/(?P<pk>[0-9]+)/$', RestCategoryDetail.as_view()),
    # Transactions
    url(r'^transaction/list',
        TransactionListView.as_view(),
        name='transaction_list'),
    url(r'^transaction/add$',
        login_required(TransactionAddView.as_view()),
        name='transaction_add'),
    url(r'^transaction/(?P<pk>[\w]+)$', TransactionView.as_view(),
        name='transaction_detail'),
    url(r'^transaction/rest/list/$', RestTransactionList.as_view()),
    url(r'^transaction/rest/(?P<pk>[0-9]+)/$', RestTransactionDetail.as_view()),
    # Manufacturer
    url(r'^manufacturer/list', ManufacturerListView.as_view(),
        name='manufacturer_list'),
    url(r'^manufacturer/add', login_required(ManufacturerAddView.as_view()),
        name='manufacturer_add'),
    url(r'^manufacturer/(?P<pk>[\w]+)/update/$', login_required(
        ManufacturerUpdateView.as_view()), name='manufacturer_update'),
    url(r'^manufacturer/(?P<pk>[\w]+)$', ManufacturerView.as_view(),
        name='manufacturer_detail'),
    url(r'^manufacturer/rest/list/$', RestManufacturerList.as_view()),
    url(r'^manufacturer/rest/(?P<pk>[0-9]+)/$', RestManufacturerDetail.as_view()),
    # Distributor
    url(r'^distributor/list', DistributorListView.as_view(),
        name='distributor_list'),
    url(r'^distributor/add', login_required(DistributorAddView.as_view()),
        name='distributor_add'),
    url(r'^distributor/(?P<pk>[\w]+)/update/$',
        login_required(DistributorUpdateView.as_view()),
        name='distributor_update'),
    url(r'^distributor/(?P<pk>[\w]+)$', DistributorView.as_view(),
        name='distributor_detail'),
    url(r'^distributor/rest/list/$', RestDistributorList.as_view()),
    url(r'^distributor/rest/(?P<pk>[0-9]+)/$', RestDistributorDetail.as_view()),
    # Storage
    url(r'^storageitem/add', login_required(StorageItemAddView.as_view()),
        name='storage_item_add'),
    url(r'^storageitem/list', StorageItemListView.as_view(),
        name='storage_item_list'),
    url(r'^storageitem/(?P<pk>[\w]+)$', StorageItemDetailView.as_view(),
        name='storage_item_detail'),
    url(r'^storageitem/(?P<pk>[\w]+)/update/$', login_required(
        StorageItemUpdateView.as_view()), name='storage_item_update'),
    url(r'^storageitem/(?P<pk>[\w]+)/merge/$', login_required(
        StorageItemMergeView.as_view()), name='storage_item_merge'),
    url(r'^storageitem/(?P<pk>[\w]+)/stocktaking/$', login_required(
        StorageItemStockTakingView.as_view()), name='storage_item_stocktaking'),
    url(r'^storage/add', login_required(StoragePlaceAddView.as_view()),
        name='storage_add'),
    url(r'^storage/list', StoragePlaceListView.as_view(),
        name='storage_list'),
    url(r'^storage/(?P<pk>[\w]+)$', StoragePlaceDetailView.as_view(),
        name='storage_detail'),
    url(r'^storage/(?P<pk>[\w]+)/update/$', login_required(
        StoragePlaceUpdateView.as_view()), name='storage_update'),
    url(r'^storage/rest/list/$', RestStoragePlaceList.as_view()),
    url(r'^storage/rest/(?P<pk>[0-9]+)/$', RestStoragePlaceDetail.as_view()),
    # Storage Types
    url(r'^storagetype/list', StorageTypeListView.as_view(),
        name='storage_type_list'),
    url(r'^storagetype/add',
        login_required(StorageTypeAddView.as_view()),
        name='storage_type_add'),
    url(r'^storagetype/(?P<pk>[\w]+)$',
        StorageTypeDetailView.as_view(),
        name='storage_type_detail'),
    url(r'^storagetype/(?P<pk>[\w]+)/update/$',
        login_required(StorageTypeUpdateView.as_view()),
        name='storage_type_update'),
    url(r'^storagetype/rest/list/$', RestStorageTypeList.as_view()),
    url(r'^storagetype/rest/(?P<pk>[0-9]+)/$',
        RestStorageTypeDetail.as_view()),
]
