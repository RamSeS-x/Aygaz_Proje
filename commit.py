import subprocess

def git_push():
    # Git komutlarını çalıştırarak değişiklikleri repo'ya aktarın
    subprocess.run(["git", "add", "."])  # Tüm dosyaları ekle
    subprocess.run(["git", "commit", "-m", "Değişiklikler"])  # Commit yap
    subprocess.run(["git", "push"])  # Uzak sunucuya gönder

# Değişiklikleri repo'ya aktarmak için fonksiyonu çağırın
git_push()
