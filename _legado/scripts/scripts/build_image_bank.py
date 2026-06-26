"""
Fashion OS — construtor do banco de imagens de referência.
Uso: python3 scripts/build_image_bank.py --unsplash SUA_KEY --pexels SUA_KEY
"""
import argparse, requests, json, os, time, shutil
from pathlib import Path

CATEGORIES = {
    "vestido":            ["elegant dress editorial fashion", "midi dress woman editorial", "wrap dress fashion editorial", "slip dress minimalist"],
    "calca":              ["tailored trousers woman editorial", "wide leg pants fashion", "straight leg trousers editorial", "black trousers minimalist"],
    "camisa":             ["white shirt woman editorial fashion", "linen shirt fashion editorial", "oversized shirt woman street style"],
    "jaqueta":            ["blazer jacket woman editorial", "tailored jacket fashion", "oversized blazer street style editorial"],
    "casaco":             ["trench coat woman editorial", "wool coat fashion editorial", "overcoat minimalist street style"],
    "top-blusa":          ["blouse woman editorial fashion", "silk top editorial", "oversized top woman minimalist"],
    "legging-activewear": ["athleisure woman editorial", "leggings outfit editorial", "pilates outfit editorial street style", "activewear fashion editorial"],
    "saia":               ["midi skirt woman editorial", "a-line skirt fashion", "pleated skirt editorial fashion"],
    "conjunto":           ["matching set woman editorial", "co-ord set fashion editorial", "two piece outfit editorial"],
}

IMGS_PER_CAT = 8  # imagens por categoria por fonte

OUT_BASE  = Path(__file__).parent.parent / "fashion-os-web" / "img" / "curated"
OUT_HORDE = Path("/tmp/fashion-os-repo/img/curated")
OUT_BASE.mkdir(parents=True, exist_ok=True)
OUT_HORDE.mkdir(parents=True, exist_ok=True)

def fetch_unsplash(query, key, per_page=4):
    url = "https://api.unsplash.com/search/photos"
    params = {"query": query, "per_page": per_page, "orientation": "portrait",
              "content_filter": "high", "order_by": "relevant"}
    r = requests.get(url, params=params, headers={"Authorization": f"Client-ID {key}"}, timeout=10)
    if not r.ok: print(f"  Unsplash erro {r.status_code}"); return []
    return [{"url": p["urls"]["regular"], "thumb": p["urls"]["small"],
             "credit": p["user"]["name"], "source": "unsplash",
             "alt_description": p.get("alt_description","")} for p in r.json().get("results", [])]

def fetch_pexels(query, key, per_page=4):
    url = "https://api.pexels.com/v1/search"
    params = {"query": query, "per_page": per_page, "orientation": "portrait"}
    r = requests.get(url, params=params, headers={"Authorization": key}, timeout=10)
    if not r.ok: print(f"  Pexels erro {r.status_code}"); return []
    return [{"url": p["src"]["large"], "thumb": p["src"]["medium"],
             "credit": p["photographer"], "source": "pexels",
             "alt_description": p.get("alt","")} for p in r.json().get("photos", [])]

def download_img(url, path):
    try:
        r = requests.get(url, timeout=15, stream=True)
        if r.ok:
            with open(path, "wb") as f:
                for chunk in r.iter_content(8192): f.write(chunk)
            return True
    except: pass
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unsplash", default="")
    ap.add_argument("--pexels",   default="")
    args = ap.parse_args()

    if not args.unsplash and not args.pexels:
        print("Passe pelo menos uma chave: --unsplash KEY ou --pexels KEY")
        return

    index = []
    for cat, queries in CATEGORIES.items():
        print(f"\n[{cat}]")
        cat_imgs = []

        for query in queries:
            if args.unsplash:
                results = fetch_unsplash(query, args.unsplash, per_page=2)
                cat_imgs.extend(results)
                time.sleep(0.3)
            if args.pexels:
                results = fetch_pexels(query, args.pexels, per_page=2)
                cat_imgs.extend(results)
                time.sleep(0.3)
            if len(cat_imgs) >= IMGS_PER_CAT: break

        # Remove duplicatas por URL
        seen, unique = set(), []
        for img in cat_imgs:
            if img["url"] not in seen:
                seen.add(img["url"])
                unique.append(img)

        for i, img in enumerate(unique[:IMGS_PER_CAT]):
            fname = f"{cat}__{i+1:02d}__{img['source']}.jpg"
            for outdir in [OUT_BASE, OUT_HORDE]:
                path = outdir / fname
                if not path.exists():
                    ok = download_img(img["url"], path)
                    status = "✓" if ok else "✗"
                    print(f"  {status} {fname}")

            index.append({
                "path":     f"./img/curated/{fname}",
                "categoria": cat,
                "fonte":    img["source"],
                "credito":  img["credit"],
                "url_original": img["url"],
                "descricao": img["alt_description"],
            })

    # Salva índice
    idx_path = Path(__file__).parent.parent / "fashion-os-web" / "js" / "curated-index.json"
    idx_horde = Path("/tmp/fashion-os-repo/js/curated-index.json")
    for p in [idx_path, idx_horde]:
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\nConcluído: {len(index)} imagens salvas.")
    print(f"Índice: {idx_path}")

if __name__ == "__main__":
    main()
