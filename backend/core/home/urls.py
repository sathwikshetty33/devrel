from django.urls import path
from . import views
from .views import *
from authorization.views import *
urlpatterns = [
    path('',views.loginView,name='login-red'),
    # path('own/',ContractOwnerView.as_view(),name='own'),
    path('hospital-login/',HospitalLogin.as_view(),name='hoslog'),
    path('patient-login/',PatientLogin.as_view(),name='patlog'),
    path('doctor-login/',DoctorLogin.as_view(),name='doclog'),
    path('hospital-dashboard/<int:id>',HospitalDashboard.as_view(),name='doc-dash'),
    path('patient-dashboard/<int:id>',PatientDashboard.as_view(),name='doc-dash'),
    path('doctor-dashboard/<int:id>',DoctorDashboard.as_view(),name='doc-dash'),
    path('doctors/<int:id>', GetDoctors.as_view(), name='doctor-list'),
    path('doctors/create/', doctor_create, name='doctor-create'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor-detail'),
    path('hospital-documents/create/', hospital_document_create, name='hospital-document-create'),
    path('hospital-documents/<int:doc_id>/grant-access/', grant_hospital_access, name='grant-hospital-access'),
    path('patient-documents/create/', patient_document_create, name='patient-document-create'),
    path('patient-documents/<int:doc_id>/visibility/', change_document_visibility, name='change-document-visibility'),
    path('patient-documents/<int:id>/',PatientDoc.as_view(),name='patient-documents'),
    path('patient-document-access/<int:id>/',getPatientDocStatus.as_view(),name='patient-doc-status'),
    path('check-patient/<int:id>',checkPatient.as_view(),name='check-patient'),
    path('check-hospital/<int:id>',checkHospital.as_view(),name='check-hospital'),
    path('check-hospital-role/', HospitalRoleCheckAPIView.as_view(), name='check-hospital-role'),
    path('hospital-ledger/', HospitalLedgerAPIView.as_view(), name='hospital-ledger'),
    path('patients/search/', PatientSearchAPIView.as_view(), name='patient-search'),
    path('doctors/search/', DoctorSearchAPIView.as_view(), name='doctor-search'),
    path('hospital-patients/', hospitalPatients.as_view(), name='hospital-patients'),
    path('hospital-documents/<int:id>/',hospitalDocumetsView.as_view(), name='hospital-document'),
    path("upload/", UploadToIPFS.as_view(), name="upload_to_ipfs"),
    path('hospital-upload-document/', UploadToIPFSHospital.as_view(), name='hospital_upload_document'),
    path('patients/<int:patient_id>/documents/<str:doc_id>/', PatientDocumentView.as_view(), name='patient-document'),
    path('hospital-documents-view/<str:doc_id>/', HospitalDocumentView.as_view(), name='hospital-document-view'),
    path('hospital-document-check/<int:id>',getHospitalDocStatus.as_view(),name='hospital-document-check'),
    path('add-acc/',Accidentadd.as_view(),name='add-acc'),
    path('change-patient-document/',changepatientDocumentView.as_view(),name='change-patient-document'),
    path('change-hospital-document/', changeHospitalDocumentView.as_view(),name='change-hospital-document'),
    path('create-patient-req/',createPatientAccessreq.as_view(),name="createHospitalPatientteHospitalAccessreq"),
    path('create-hospital-req/',createHospitalAccessreq.as_view(),name="createHospitalDocumentAccess"),
    path('change-patient-access/',changePatientDocumentAccess.as_view(),name="changePatientDocumentAccess"),
    path('change-hospital-acces/',changeHospitalDocumentAccess.as_view(),name="changeHospitalDocumentAccess"),
    path('decline-patient-req/',declinePatientDocumentReq.as_view(),name="declinePatientDocumentReq"),
    path('decline-hospital-request/',declineHospitalDocumentReq.as_view(),name="declineHospitalDocumentReq"),
    path('patient-req-list/',PatientDocumentRequestList.as_view(),name="PatientDocumentRequestList"),
    path('hospital-request-list',HospitalDocumentRequestList.as_view(),name="HospitalDocumentRequestList"),
    path('delete-patient-document/',deletePatientDocument.as_view(),name="deletePatientDocument"),
    path('delete-hospital-document/',deleteHospitalDocument.as_view(),name="deleteHospitalDocument"),
    path('document-processes/', DocumentProcessStatusView.as_view(), name='document_processes'),

    ]