#!/bin/bash
# Çift tıkla: bu klasördeki tüm değişiklikleri GitHub'a gönderir.
cd "$(dirname "$0")" || exit 1
git add -A
if git diff --cached --quiet; then
  echo "Yeni değişiklik yok."
else
  git commit -q -m "Güncelleme: $(date '+%Y-%m-%d %H:%M')" && echo "Değişiklikler kaydedildi."
fi
if git push -q; then echo "Tamam! GitHub güncellendi. 🦄🌈"; else echo "Gönderilemedi. İnternet bağlantısını ve 'gh auth login' girişini kontrol edin."; fi
sleep 4
