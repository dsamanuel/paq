from django.urls import path, include

from . import views




urlpatterns = [
   
    path('', views.conceptnotes, name='icns'),
    path('intervention/', views.conceptnotes, name='icns'),
    path('intervention/new', views.icn_add, name='icn_new'),
    path('intervention/<int:id>/edit/', views.icn_edit, name='icn_edit'),


    path('icn/add', views.icn_add, name='icn_add'),
    path('intervention/<int:pk>/', views.icn_detail, name='icn_detail'),
    path('intervention/<int:pk>/approval/', views.icn_submit_approval, name='icn_submit_approval'),
    path('activity/<int:pk>/approval/', views.activity_submit_approval, name='activity_submit_approval'),
    path('download/<int:id>/', views.download, name='download'),
    path('downloada/<int:id>/', views.downloada, name='downloada'),
    path('delete_icn/<int:pk>/', views.icn_delete, name='icn_delete'),
    
    #path('iregion/', views.iregion, name='iregion'),
    #path('iregion/izones/', views.izones, name='izones'),
    path('iregion/<int:id>/', views.iregion, name='iregion'),
    path('iregion/izones/', views.izones, name='izones'),
    path('iregion/izones/iworedas/', views.iworedas, name='iworedas'),
    path('idelete_iarea/<int:pk>/', views.idelete_area, name='idelete_area'),
    path('adelete_aarea/<int:pk>/', views.adelete_area, name='adelete_aarea'),
    path('iregion/iedit_iarea/<int:pk>/', views.iarea_edit_form, name='iarea_edit_form'),
    path('download_env_att/<int:id>/', views.download_env_att, name='download_env_att'),
    path('icn_submit_form_partial/<int:id>/', views.icn_submit_form_partial, name='icn_submit_form_partial'),
    path('activity_submit_form_partial/<int:id>/', views.activity_submit_form_partial, name='activity_submit_form_partial'),
    path('activity/', views.activities, name='activities'),
    path('activity/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('activity/add', views.activity_add, name='activity_new'),
    path('activity/<int:id>/edit/', views.activity_edit, name='activity_edit'),
    path('aregion/<int:id>/', views.aregion, name='aregion'),
    path('aregion/aedit_aarea/<int:pk>/', views.aarea_edit_form, name='aarea_edit_form'),
    
]

htmxpatterns = [


 
 path('icn_submit_detail/<int:id>/', views.icn_submit_detail, name='icn_submit_detail'),
 path('icn_submit_list/<int:id>/', views.icn_submit_list, name='icn_submit_list'),


 path('icn_submit_form/<int:id>/', views.icn_submit_form, name='icn_submit_form'),
 path('activity_submit_form/<int:id>/', views.activity_submit_form, name='activity_submit_form'),
 path('icn_submit_document/<int:id>/', views.icn_submit_document, name='icn_submit_document'),
 path('activity_submit_document/<int:id>/', views.activity_submit_document, name='activity_submit_document'),
 path('icn_approvalp/<int:id>/', views.icn_approvalp, name='icn_approvalp'),
 path('icn_approvalf/<int:id>/', views.icn_approvalf, name='icn_approvalf'),
 path('icn_approvalt/<int:id>/', views.icn_approvalt, name='icn_approvalt'),
 path('activity_approvalt/<int:id>/', views.activity_approvalt, name='activity_approvalt'),
 path('activity_approvalp/<int:id>/', views.activity_approvalp, name='activity_approvalp'),
 path('activity_approvalf/<int:id>/', views.activity_approvalf, name='activity_approvalf'),
 path('icn_filter/', views.search_results_view, name='icn_filter'),
 path('activity_filter/', views.search_results_view2, name='activity_filter'),
 
 path('document_list/<int:id>/', views.document_list, name='document_list'),
 path('activity_document_list/<int:id>/', views.activity_document_list, name='activity_document_list'),
 path('iarea_list/<int:id>/', views.iarea_list, name='iarea_list'),
 path('aarea_list/<int:id>/', views.aarea_list, name='aarea_list'),
 path('current_submit_approval_list/<int:id>/', views.current_submit_approval_list, name='current_submit_approval_list'),
 path('current_activity_submit_approval_list/<int:id>/', views.current_activity_submit_approval_list, name='current_activity_submit_approval_list'),
 path('submit_approval_list/<int:id>/', views.submit_approval_list, name='submit_approval_list'),
 path('activity_submit_approval_list/<int:id>/', views.activity_submit_approval_list, name='activity_submit_approval_list'),
 path('add_impact/<int:id>/', views.add_impact, name='add_impact'),
 path('add_activity_impact/<int:id>/', views.add_activity_impact, name='add_activity_impact'),
 path('impact_list/<int:id>/', views.impact_list, name='impact_list'),
 path('activity_impact_list/<int:id>/', views.activity_impact_list, name='activity_impact_list'),
 path('edit_impact/<int:pk>/', views.edit_impact, name='edit_impact'),
 path('edit_activity_impact/<int:pk>/', views.edit_activity_impact, name='edit_activity_impact'),
 path('impact/<int:pk>/remove', views.remove_impact, name='remove_impact'),
 path('activity_impact/<int:pk>/remove', views.remove_activity_impact, name='remove_activity_impact'),
]

urlpatterns += htmxpatterns