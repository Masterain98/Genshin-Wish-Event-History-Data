from utils import get_all_pools
import json


if __name__ == '__main__':
    main_dict = list(get_all_pools().values())
    with open("pool.json", "w", encoding="utf-8") as f:
        json.dump(main_dict, f, ensure_ascii=False, indent=4, default=str)
