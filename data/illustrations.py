fields_map = {
    "authfull": "作者全名",
    "inst_name": "所在机构名称",
    "cntry": "所在国家或地区",
    "np6022": "论文数量（1960~2022）",
    "firstyr": "首次发表年份",
    "lastyr": "最后发表年份",
    "rank(ns)": "排名（不含）",
    "nc9622(ns)": "发表论文数（1996~2022，不含）",
    "h22(ns)": "h指数（2022，不含）",
    "hm22(ns)": "hm指数（2022，不含）",
    "nps(ns)": "发表论文数（不含）",
    "ncs(ns)": "论文被引次数（不含）",
    "cpsf(ns)": "论文数+合著数（不含）",
    "ncsf(ns)": "合著数+合著作者数（不含）",
    "npsfl(ns)": "领域论文被引次数（不含）",
    "ncsfl(ns)": "领域合著论文被引次数（不含）",
    "c(ns)": "论文平均被引次数（不含）",
    "npciting(ns)": "论文（2022）被引次数（不含）",
    "cprat(ns)": "被引论文比例（不含）",
    "np6022_cited9622(ns)": "论文（1960~2022）被引数（1996~2022，不含）",
    "self%": "自引比例",
    "rank": "排名",
    "nc9622": "发表论文数（1996~2022）",
    "h22": "h指数（2022）",
    "hm22": "hm指数（2022）",
    "nps": "发表论文数",
    "ncs": "论文被引次数",
    "cpsf": "论文数+合著数",
    "ncsf": "合著数+合著作者数",
    "npsfl": "领域论文被引次数",
    "ncsfl": "领域合著论文被引次数",
    "c": "论文平均被引次数",
    "npciting": "论文（2022）被引次数",
    "cprat": "被引论文比例",
    "np6022_cited9622": "论文（1960~2022）被引数（1996~2022）",
    "np6022_d": "从Scopus中删除的论文数（1960~2022）",
    "np9622_d": "从Scopus中删除的论文数（1996~2022）",
    "sm_subfield_1": "学科子领域1",
    "sm_subfield_1_frac": "学科子领域1的百分比",
    "sm_subfield_2": "学科子领域2",
    "sm_subfield_2_frac": "学科子领域2的百分比",
    "sm_field": "学科领域",
    "sm_field_frac": "学科领域的百分比",
    "rank_sm_subfield_1": "学科子领域1排名",
    "rank_sm_subfield_1(ns)": "学科子领域1排名（不含）",
    "sm_subfield_1_count": "学科子领域1的论文数量"
}

country_map = {
    'are': '阿拉伯联合酋长国',
    'srb': '塞尔维亚',
    'fra': '法国',
    'eth': '埃塞俄比亚',
    'kna': '圣基茨和尼维斯',
    'mng': '蒙古',
    'vnm': '越南',
    'mex': '墨西哥',
    'tun': '突尼斯',
    'scg': '塞尔维亚和黑山',
    'ury': '乌拉圭',
    'cod': '刚果民主共和国',
    'rwa': '卢旺达',
    'ita': '意大利',
    'est': '爱沙尼亚',
    'alb': '阿尔巴尼亚',
    'nor': '挪威',
    'hrv': '克罗地亚',
    'moz': '莫桑比克',
    'pse': '巴勒斯坦',
    'afg': '阿富汗',
    'fji': '斐济',
    'bih': '波黑',
    'grl': '格陵兰',
    'yem': '也门',
    'mys': '马来西亚',
    'guf': '法属圭亚那',
    'can': '加拿大',
    'lva': '拉脱维亚',
    'gha': '加纳',
    'ncl': '新喀里多尼亚',
    'tza': '坦桑尼亚',
    'rus': '俄罗斯',
    'mwi': '马拉维',
    'isl': '冰岛',
    'mrt': '毛里塔尼亚',
    'mus': '毛里求斯',
    'hti': '海地',
    'gbr': '英国',
    'tur': '土耳其',
    'svk': '斯洛伐克',
    'nga': '尼日利亚',
    'brn': '文莱',
    'isr': '以色列',
    'dza': '阿尔及利亚',
    'bhr': '巴林',
    'ant': '荷属安的列斯',
    'dma': '多米尼克',
    'brb': '巴巴多斯',
    'zaf': '南非',
    'geo': '格鲁吉亚',
    'lao': '老挝',
    'hkg': '香港',
    'irq': '伊拉克',
    'esp': '西班牙',
    'irn': '伊朗',
    'kaz': '哈萨克斯坦',
    'swz': '斯威士兰',
    'jam': '牙买加',
    'npl': '尼泊尔',
    'aus': '澳大利亚',
    'chl': '智利',
    'kwt': '科威特',
    'zwe': '津巴布韦',
    'lbr': '利比里亚',
    'lie': '列支敦士登',
    'cmr': '喀麦隆',
    'pri': '波多黎各',
    'che': '瑞士',
    'egy': '埃及',
    'csk': '捷克斯洛伐克',
    'ven': '委内瑞拉',
    'kir': '基里巴斯',
    'chn': '中国',
    'gtm': '危地马拉',
    'pol': '波兰',
    'reu': '留尼汪',
    'smr': '圣马力诺',
    'zmb': '赞比亚',
    'bra': '巴西',
    'mmr': '缅甸',
    'bmu': '百慕大',
    'mac': '澳门',
    'tls': '东帝汶',
    'jpn': '日本',
    'idn': '印度尼西亚',
    'lbn': '黎巴嫩',
    'per': '秘鲁',
    'lka': '斯里兰卡',
    'ltu': '立陶宛',
    'tto': '特立尼达和多巴哥',
    'lby': '利比亚',
    'grd': '格林纳达',
    'cri': '哥斯达黎加',
    'mkd': '北马其顿',
    'ecu': '厄瓜多尔',
    'mdg': '马达加斯加',
    'cyp': '塞浦路斯',
    'omn': '阿曼',
    'jor': '约旦',
    'pak': '巴基斯坦',
    'twn': '台湾',
    'bdi': '布隆迪',
    'phl': '菲律宾',
    'pry': '巴拉圭',
    'syr': '叙利亚',
    'bel': '比利时',
    'sen': '塞内加尔',
    'dnk': '丹麦',
    'fin': '芬兰',
    'kgz': '吉尔吉斯斯坦',
    'sgp': '新加坡',
    'grc': '希腊',
    'aut': '奥地利',
    'mlt': '马耳他',
    'ken': '肯尼亚',
    'uga': '乌干达',
    'rou': '罗马尼亚',
    'arm': '亚美尼亚',
    'civ': '科特迪瓦',
    'nld': '荷兰',
    'aze': '阿塞拜疆',
    'usa': '美国',
    'mli': '马里',
    'ind': '印度',
    'gnb': '几内亚比绍',
    'irl': '爱尔兰',
    'mar': '摩洛哥',
    'flk': '福克兰群岛',
    'hnd': '洪都拉斯',
    'arg': '阿根廷',
    'mda': '摩尔多瓦',
    'hun': '匈牙利',
    'sau': '沙特阿拉伯',
    'and': '安道尔',
    'fro': '法罗群岛',
    'sux': '苏格兰',
    'prt': '葡萄牙',
    'sle': '塞拉利昂',
    'col': '哥伦比亚',
    'deu': '德国',
    'ben': '贝宁',
    'bwa': '博茨瓦纳',
    'swe': '瑞典',
    'mco': '摩纳哥',
    'blr': '白俄罗斯',
    'cub': '古巴',
    'uzb': '乌兹别克斯坦',
    'kor': '韩国',
    'nam': '纳米比亚',
    'cze': '捷克',
    'qat': '卡塔尔',
    'bgd': '孟加拉国',
    'pan': '巴拿马',
    'lso': '莱索托',
    'vut': '瓦努阿图',
    'pyf': '法属波利尼西亚',
    'khm': '柬埔寨',
    'lux': '卢森堡',
    'nzl': '新西兰',
    'svn': '斯洛文尼亚',
    'ukr': '乌克兰',
    'gmb': '冈比亚',
    'sdn': '苏丹',
    'nan': '南极洲',
    'bhs': '巴哈马',
    'bgr': '保加利亚',
    'mne': '黑山',
    'tha': '泰国'
}


