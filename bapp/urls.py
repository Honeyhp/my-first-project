from django.urls import path
from . import views
urlpatterns=[
    path('',views.homefn),
    path('login/',views.login),
    path('coach_login',views.clogin),
    path('owner_home',views.ohome),
    path('coach_home',views.chome),
    path('Addcoach_info',views.coainfo),
    path('coach_info',views.coachinfo),
    path('display_coach',views.displaycoach),
    path('view_coach/<int:id>',views.vicoach),
    path('Edit_coach/<int:id>',views.editcoach),
    path('Edit_coach/Edit_coach/<int:id>',views.editcoach),
    path('logout',views.logout),
    path('contact',views.contact),
    path('coach_logout',views.coachlogout),
    path('Delete/<int:id>',views.delete),
    path('Team_Report',views.tmreport),
    path('player_report',views.playreport),
    path('Player_info',views.player),
    path('schedule_report',views.schedulereport),
    path('man_match_report',views.matchreport),
    path('winloss_report',views.winlossreport),
    path('display_player',views.displayplayer),
    path('view_player/<int:id>',views.viewplayer),
    path('Edit_player/<int:id>',views.editplayer),
    path('Edit_player/Edit_player/<int:id>',views.editplayer),
    path('Delete_player/<int:id>',views.deleteplayer),
    path('Team',views.team),
    path('display_team',views.displayteam),
    path('Edit_team/<int:id>',views.editteam),
    path('Delete_team/<int:id>',views.deleteteam),
    path('Assign_team',views.assigntm),
    path('Edit_assigntm/<int:id>',views.editassign),
    path('Edit_assigntm/Edit_assigntm/<int:id>',views.editassign),
    path('Delete_assigntm/<int:id>',views.delete_assigntm),
    path('display_assigntm',views.disassigntm),
    path('View_Team',views.viewteam),
    path('view_team_player',views.viewteamply),
    path('forgot_password',views.forgotpwd),
    path('otp_verify',views.otpverify),
    path('schedule',views.schedule),
    path('Edit_schedule/<int:id>',views.editschedule),
    path('display_schedule',views.displayschedule),
    path('Delete_schedule/<int:id>',views.deleteschedule),
    path('player_login',views.playerlogin),
    path('player_home',views.plyhome),
    path('Players_schedule/<int:id>',views.plyschedule),
    path('contact_ply',views.contactply),
    path('plylogout',views.plylogout),
    path('ply_forgotpwd',views.plyforgotpwd),
    path('otpverify',views.otpverify1),
    path('display_Allplayer',views.allplayer)
]