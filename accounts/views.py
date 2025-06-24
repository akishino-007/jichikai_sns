from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from allauth.account.views import ConfirmEmailView


@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        user.last_name = request.POST.get('last_name', '')
        user.first_name = request.POST.get('first_name', '')
        birthyear = request.POST.get('birthyear')
        kumi = request.POST.get('kumi')

        # バリデーション（必要に応じて追加）
        if birthyear:
            user.birthyear = int(birthyear)
        if kumi:
            user.kumi = int(kumi)

        user.save()
        messages.success(request, 'プロフィールを保存しました！')
        return redirect('account_login')  # 'account_login' は URL 名（urls.pyで確認）

    return render(request, 'account/profile.html', {'user': user})

class CustomConfirmEmailView(ConfirmEmailView):
    def post(self, *args, **kwargs):
        print("✅ CustomConfirmEmailView activated!")  # ← 確認用ログ出力
        confirmation = self.get_object()
        confirmation.confirm(self.request)

        # 自動ログイン
        user = confirmation.email_address.user
         # 🔽 認証バックエンドを明示的に指定
        user.backend = 'django.contrib.auth.backends.ModelBackend'

        login(self.request, user)

        return redirect('accounts:profile')

