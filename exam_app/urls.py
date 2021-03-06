from django.urls import path
from . import views

app_name = "exam_app"
urlpatterns = [
    path('create-exam/', views.createExam, name="create-exam"),
    path('instructors/all-exams/', views.viewAllExamsInstructors, name="view-all-exams-instructors"),
    path('edit-exam/<int:exam_id>/', views.editExam, name="edit-exam"),
    path('edit-exam/<int:exam_id>/add-question/', views.addQuestion, name="add-question"),
    path('edit-exam/<int:exam_id>/edit-question/<int:question_id>/', views.EditQuestion, name="edit-question"),
    path('tutee/all-exams/', views.viewAllExamsTutee, name="view-all-exams-tutee"),
    path('view-exam/<int:exam_id>/', views.viewExam, name="view-exam"),
    path('exam-summary/<int:exam_details_id>', views.examSummary, name="exam-summary"),
    path('exam-result/<int:exam_details_id>', views.examResult, name="exam-result"),
    path('exam-results-list/<int:exam_id>', views.examResultsList, name="tutee-exam-results-list"),
    path('<int:exam_details_id>/view_question_result/<int:question_details>', views.questionResult,
         name="question-result"),
    path('edit-exam/edit-details/<int:exam_id>', views.editExamDetails, name="edit-details"),
    path('instructor/<int:exam_id>/results/', views.viewAllDetails, name="instructor-details"),
    path('instructor/<int:exam_id>/results/<int:exam_details_id>', views.tuteeExamDetails, name="tutee-exam-results"),
    path('exam/<int:exam_details_id>/evaluation/<int:question_details_id>', views.questionEvaluation,
         name='question-evaluation'),
    path('edit-exam/<int:exam_id>/add-section/', views.addSection, name="add-section"),
    path('edit-exam/<int:exam_id>/edit-section/<int:section_id>', views.editSection, name="edit-section"),
    path('edit-exam/<int:exam_id>/section/<int:section_id>/add-question', views.sectionAddQuestion,
         name="section-add-question"),
    path('edit-exam/<int:exam_id>/section/<int:section_id>/edit-question/<int:question_id>', views.sectionEditQuestion,
         name="section-edit-question"),
    path('<int:exam_id>/<int:section_index>/<int:question_index>', views.takeExamSection, name="take-exam-section"),
]
