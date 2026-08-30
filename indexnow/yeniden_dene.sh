#!/usr/bin/env bash
# IndexNow anahtari yeni olusturuldugunda dogrulama gecikmeli olur.
# Once tek URL ile dogrulama durumunu yoklar; gecince tam listeyi gonderir.
K=1830a2386a4abf806481442d83b9582f
RUN="$HOME/.claude/skills/seo/bin/claude-seo"
cd "$(dirname "$0")/.."

for tur in 1 2 3 4 5 6; do
  echo "--- deneme $tur ($(date +%H:%M:%S)) ---"
  ok=1
  for h in huneducation.com tr.huneducation.com; do
    yanit=$("$RUN" run indexnow_submit.py --host "$h" --key "$K" \
            --key-location "https://$h/$K.txt" --urls "https://$h/" --json 2>&1)
    kod=$(echo "$yanit" | PYTHONIOENCODING=utf-8 python -c "import sys,json;print(json.load(sys.stdin).get('status_code'))" 2>/dev/null)
    echo "  $h yoklama: $kod"
    [ "$kod" = "200" ] || [ "$kod" = "202" ] || ok=0
    sleep 3
  done
  if [ "$ok" = "1" ]; then
    echo "DOGRULAMA GECTI - tam liste gonderiliyor"
    for h in huneducation.com tr.huneducation.com; do
      echo "=== $h ($(wc -l < indexnow/$h.txt) URL) ==="
      "$RUN" run indexnow_submit.py --host "$h" --key "$K" \
         --key-location "https://$h/$K.txt" --urls-file "indexnow/$h.txt" --json 2>&1 | head -12
      sleep 5
    done
    echo "TAMAMLANDI"
    exit 0
  fi
  echo "  henuz dogrulanmadi, 5 dk bekleniyor"
  sleep 300
done
echo "ALTI DENEMEDE DOGRULANMADI - anahtar dosyasi yerinde, sonra tekrar denenmeli"
exit 1
