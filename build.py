#!/usr/bin/env python3
"""Static site generator for nabla-b.engineering.

Usage:  python3 build.py          (writes HTML into the repo root, en/ and zh/)
All content lives in this file (see CONTENT below). No dependencies.
"""
import json, os, html, datetime

BASE = "https://nabla-b.engineering"
ORG_ID = BASE + "/#organization"
PERSON_STEPHAN = "https://maxclerkwell.tech/#person"
PERSON_TABEA = "https://edge-compute.skainet.io/team#tabea-boekelmann"
PERSON_MEIHUI = BASE + "/team/#meihui-huang"
PERSON_VANESSA = BASE + "/team/#vanessa-wilcken"
PERSON_ATIYEH = BASE + "/team/#atiyeh-chatrsefid"
MAIL_ATIYEH = "atiyeh.chatrsefid@nabla-b.engineering"
AUTOINTERN_ID = "https://www.auto-intern.de/#organization"
AIGRUPPE_ID = "https://gruppe.ai/#brand"
EDGE_PRODUCT_ID = "https://edge-compute.skainet.io/#product"
TODAY = datetime.date.today().isoformat()

TEL = "+49 234 58545811"
TEL_HREF = "tel:+4923458545811"
MAIL = "office@nabla-b.engineering"

LANGS = {"de": "", "en": "en/", "zh": "zh/"}
PAGES = ["index", "leistungen", "referenzen", "team", "kontakt", "impressum", "datenschutz"]
SLUGS = {  # slug per language
    "de": {"index": "", "leistungen": "leistungen/", "referenzen": "referenzen/", "team": "team/", "kontakt": "kontakt/", "impressum": "impressum/", "datenschutz": "datenschutz/"},
    "en": {"index": "", "leistungen": "services/", "referenzen": "references/", "team": "team/", "kontakt": "contact/", "impressum": "imprint/", "datenschutz": "privacy/"},
    "zh": {"index": "", "leistungen": "services/", "referenzen": "references/", "team": "team/", "kontakt": "contact/", "impressum": "imprint/", "datenschutz": "privacy/"},
}
def url(lang, page): return BASE + "/" + LANGS[lang] + SLUGS[lang][page]
def path(lang, page): return "/" + LANGS[lang] + SLUGS[lang][page]

# ---------------------------------------------------------------- references
REFS = [
 dict(key="edge", years="2016 – 2026", client="Auto-Intern GmbH / skAInet",
  de=("skAInet Edge-Compute", "Programmierbarer M12-PoE-Switch, Router und Linux-Rechenknoten für industrielle Edge-Datenerfassung: 7 gedichtete PoE-Ports, 8-Kern-ARM, Yocto Linux mit dokumentierter SBOM. Systemarchitektur, PoE-first-Konzept, M12-Verkabelungsspezifikation und EMV-Zertifizierung."),
  en=("skAInet Edge-Compute", "Programmable M12-PoE switch, router and Linux compute node for industrial edge data acquisition: 7 sealed PoE ports, 8-core ARM, Yocto Linux with documented SBOM. System architecture, PoE-first concept, M12 cabling specification and EMC certification."),
  zh=("skAInet Edge-Compute 边缘计算平台", "面向工业边缘数据采集的可编程 M12-PoE 交换机、路由器与 Linux 计算节点：7 个密封 PoE 端口、8 核 ARM、带完整 SBOM 的 Yocto Linux。负责系统架构、PoE 优先设计、M12 布线规范与 EMC 认证。"),
  links=[("edge-compute.skainet.io","https://edge-compute.skainet.io/"),("Blog","https://maxclerkwell.tech/posts/skainet-edge-compute-september-2026/")]),
 dict(key="reflow", years="2022 – laufend", client="Kurtz Ersa / globalPoint ICS",
  de=("globalPoint horus® – Reflow-Profiling & Monitoring", "Messelektronik und Monitoring-Infrastruktur für die Lötprofil-Erstellung und die kontinuierliche Prozessüberwachung an Reflow-Öfen (Productronica Innovation Award 2023): batteriebetriebene Temperaturprofil-Elektronik mit WLAN, Telemetrie- und Observability-Stack für die prädiktive Bewertung von Lötqualitätsfaktoren, Cloud-Anbindung. Inklusive EMV-Zertifizierung in China."),
  en=("globalPoint horus® — reflow profiling & monitoring", "Measurement electronics and monitoring infrastructure for solder-profile creation and continuous process monitoring on reflow ovens (Productronica Innovation Award 2023): battery-powered temperature-profiling electronics with Wi-Fi, telemetry and observability stack for predictive assessment of solder-quality factors, cloud integration. Including EMC certification in China."),
  zh=("globalPoint horus® – 回流焊温度曲线与过程监测", "用于回流焊炉焊接曲线创建与持续过程监测的测量电子与监测基础设施（2023 年 Productronica 创新奖）：带 Wi-Fi 的电池供电温度曲线电子设备、用于焊接质量预测评估的遥测与可观测性栈、云端集成。含在中国完成的 EMC 认证。"),
  links=[("horus® Software","https://gp-ics.com/products/horus-software/"),("horus® Shuttle","https://gp-ics.com/products/horus-shuttle/"),("Award-News","https://gp-ics.com/news/globalpoint-horus-profiling-state-of-the-art-measuring-electronics-for-fastest-profiling/"),("EMV-Story","https://maxclerkwell.tech/posts/dongguan-emc-march-2026/")]),
 dict(key="omnai", years="2020 – 2024", client="autowerkstatt4null (BMWK)",
  de=("OmnAIScope", "Vereinfachtes digitales Oszilloskop, das Signaldiagnose für die Kfz-Werkstatt alltagstauglich macht. Entstanden im Forschungsprojekt aw4null, Patent angemeldet."),
  en=("OmnAIScope", "Simplified digital oscilloscope that makes waveform diagnostics usable in everyday automotive workshop practice. Grown out of the aw4null research programme, patent pending."),
  zh=("OmnAIScope 示波器", "简化型数字示波器，让汽修车间能在日常工作中使用波形诊断。源于 aw4null 研究项目，专利申请中。"),
  links=[("Blog","https://maxclerkwell.tech/posts/omnaiscope-august-2025/")]),
 dict(key="msu", years="2023 – 2026", client="Montana State University",
  de=("Resonanzspektroskop für Biofilm-Monitoring", "Embedded-Instrumentierung für elektrochemische Impedanzspektroskopie im Feld – erfasst Biofilme in Flusssystemen quer durch die USA."),
  en=("Resonance spectroscope for biofilm monitoring", "Embedded instrumentation for electrochemical impedance spectroscopy in the field — detecting biofilms in river systems across the continental US."),
  zh=("生物膜监测共振谱仪", "用于野外电化学阻抗谱的嵌入式仪器——在美国各河流系统中检测生物膜。"),
  links=[("Feldbericht","https://maxclerkwell.tech/posts/msu-eis-2024/")]),
 dict(key="hvmaps", years="2020 – 2026", client="Ruhr-Universität Bochum / PANDA @ FAIR",
  de=("HV-MAPS-Teststände & Drahtbond-Linie", "Mehrere Teststände zur Charakterisierung von HV-MAPS-Siliziumsensoren für minimal ionisierende Teilchen sowie Aufbau einer Drahtbond-Produktionslinie."),
  en=("HV-MAPS test stands & wire-bonding line", "Multiple test stands for characterising HV-MAPS silicon sensors for minimum-ionizing particles, plus building up a wire-bonding production line."),
  zh=("HV-MAPS 测试台与引线键合产线", "多个用于表征最小电离粒子 HV-MAPS 硅传感器的测试台，以及引线键合生产线的搭建。"),
  links=[("Geant4-Simulation","https://maxclerkwell.tech/posts/hv-maps-energy-loss-simulation-may-2026/"),("KiCon Asia Talk","https://maxclerkwell.tech/posts/kicon-asia-2025/")]),
 dict(key="zynq", years="seit 2026", client="Open Source",
  de=("Zynq-Bitstream-Pipeline (ALINX AX7020)", "Offener Weg vom JTAG-Bring-up ohne FSBL über mainline U-Boot bis zu einem Yocto Linux im QSPI-Flash, das seine eigenen Updates holt – Hardware deployen wie Software."),
  en=("Zynq bitstream pipeline (ALINX AX7020)", "Open path from JTAG bring-up without FSBL via mainline U-Boot to a Yocto Linux in QSPI flash that fetches its own updates — deploying hardware like software."),
  zh=("Zynq 比特流部署流水线（ALINX AX7020）", "从无 FSBL 的 JTAG 启动、主线 U-Boot，到能自行拉取更新的 QSPI Yocto Linux 的开源路径——像部署软件一样部署硬件。"),
  links=[("Konzept","https://maxclerkwell.tech/posts/zynq-bitstream-deployment-concept-august-2026/"),("Bring-up","https://maxclerkwell.tech/posts/alinx-bring-up-jtag-detected-without-power-august-2026/"),("Yocto/QSPI","https://maxclerkwell.tech/posts/alinx-ax7020-yocto-linux-qspi-august-2026/")]),
 dict(key="powersense", years="2020 – 2025", client="skAInet / DB Netz AG",
  de=("PowerSense – Monitoring kritischer Infrastruktur", "Stromsensorik und Analyse für Weichendiagnose und Zustandsüberwachung, u. a. im DIANA-System der Deutschen Bahn."),
  en=("PowerSense — critical infrastructure monitoring", "Current sensing and analytics for railway-switch diagnostics and condition monitoring, e.g. in Deutsche Bahn's DIANA system."),
  zh=("PowerSense 关键基础设施监测", "用于道岔诊断与状态监测的电流传感与分析，应用于德国铁路 DIANA 系统等。"),
  links=[("10 Jahre PowerSense","https://maxclerkwell.tech/posts/skainet-powersense-jan-2026/")]),
 dict(key="vision", years="2026", client="NDA",
  de=("Embedded-Vision-System mit KI-Beschleunigung", "PCB-Design für ein eingebettetes Bildverarbeitungssystem mit KI-Beschleuniger. Kunde unter NDA."),
  en=("Embedded vision system with AI acceleration", "PCB design for an embedded vision system with an AI accelerator. Customer under NDA."),
  zh=("带 AI 加速的嵌入式视觉系统", "为带 AI 加速器的嵌入式视觉系统进行 PCB 设计。客户受保密协议约束。"),
  links=[]),
 dict(key="enclosure", years="2022", client="Patent angemeldet",
  de=("Gehäuselose Gehäuse", "Gehäuselose Bauform für Leiterplatten-Kavitäten – Mechanik, EMV und Fertigung in einem Konzept."),
  en=("Enclosureless housings", "Enclosureless design for PCB cavities — mechanics, EMC and manufacturing in one concept."),
  zh=("无外壳封装", "面向 PCB 腔体的无外壳结构——将机械、EMC 与制造整合为一个方案。"),
  links=[("Funktionsweise","https://maxclerkwell.tech/posts/enclosureless-cases-april-2026/")]),
 dict(key="mineberry", years="2023 – 2025", client="RAG / Forschungszentrum Nachbergbau",
  de=("MineBerry-LoRa – Geomonitoring", "Bewertung der Standsicherheit von Schachtverschlüssen mit LoRa-Sensorik und Multi-Sensor-Datenfusion."),
  en=("MineBerry-LoRa — geomonitoring", "Structural-stability assessment of mine-shaft closures with LoRa sensors and multi-sensor data fusion."),
  zh=("MineBerry-LoRa 地质监测", "利用 LoRa 传感器与多传感器数据融合评估矿井封闭结构的稳定性。"),
  links=[]),
 dict(key="kelvion", years="2023", client="Kelvion",
  de=("Infrarot-Interferometriekamera für Luftkühler", "Kamerasystem zur Fern-Bewertung der Verschmutzung (Fouling) von Air-Fin-Coolern – Optik, Embedded-Elektronik und Auswertung für den Einsatz an Industrieanlagen."),
  en=("Infrared interferometry camera for air-fin coolers", "Camera system for remote assessment of fouling on air-fin coolers — optics, embedded electronics and analysis for use on industrial plants."),
  zh=("空冷器红外干涉相机", "用于远程评估空冷器（air-fin cooler）污垢程度的相机系统——光学、嵌入式电子与分析，面向工业装置现场应用。"),
  links=[]),
 dict(key="rain", years="2021", client="25square",
  de=("Starkregen-Messnetz", "PoE-basiertes Mess- und Analysesystem zur Beobachtung und Vorhersage von Starkregenzellen. Patent angemeldet."),
  en=("Heavy-rain sensor network", "PoE-based measurement and analysis system for observing and predicting heavy-rain cells. Patent pending."),
  zh=("强降雨监测网络", "基于 PoE 的测量与分析系统，用于观测和预测强降雨单元。专利申请中。"),
  links=[]),
]

# ---------------------------------------------------------------- ui strings
UI = {
 "de": dict(nav=[("index","Start"),("leistungen","Leistungen"),("referenzen","Referenzen"),("team","Team"),("kontakt","Kontakt")],
   legal=[("impressum","Impressum"),("datenschutz","Datenschutz")], menu="Menü",
   footer_contact="Kontakt", footer_hours="Bürozeiten: Mo – Fr, 9:00 – 13:30 Uhr", footer_office="Ansprechpartnerin: Vanessa Wilcken",
   footer_group="nabla B ist Teil der <a href=\"https://gruppe.ai/\">AI-Gruppe</a>.", footer_blog="Technischer Blog: <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a>",
   copyright="© {y} nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)", cd="Corporate-Design-Handbuch (PDF)",
   ref_title="Willkommen bei nabla B.", ref_text="Sie kommen von maxclerkwell.tech, dem Blog von Stephan Bökelmann. nabla B ist sein Ingenieurbüro in Bochum; über diese Firma werden die im Blog beschriebenen Projekte beauftragt. Hier finden Sie Leistungen, Team, Referenzen und Kontakt.", ref_ok="Verstanden", ref_back="Zurück zum Blog"),
 "en": dict(nav=[("index","Home"),("leistungen","Services"),("referenzen","References"),("team","Team"),("kontakt","Contact")],
   legal=[("impressum","Imprint"),("datenschutz","Privacy")], menu="Menu",
   footer_contact="Contact", footer_hours="Office hours: Mon – Fri, 9:00 – 13:30 CET", footer_office="Your contact: Vanessa Wilcken",
   footer_group="nabla B is part of the <a href=\"https://gruppe.ai/\">AI-Gruppe</a>.", footer_blog="Technical blog: <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a>",
   copyright="© {y} nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)", cd="Corporate design manual (PDF, German)",
   ref_title="Welcome to nabla B.", ref_text="You came from maxclerkwell.tech, Stephan Bökelmann’s blog. nabla B is his engineering office in Bochum, the company through which the projects described on the blog are contracted. Here you find services, team, references and contact.", ref_ok="Got it", ref_back="Back to the blog"),
 "zh": dict(nav=[("index","首页"),("leistungen","服务"),("referenzen","项目案例"),("team","团队"),("kontakt","联系")],
   legal=[("impressum","法律声明"),("datenschutz","隐私政策")], menu="菜单",
   footer_contact="联系方式", footer_hours="办公时间：周一至周五 9:00 – 13:30（中欧时间）", footer_office="联系人：Vanessa Wilcken",
   footer_group="nabla B 是 <a href=\"https://gruppe.ai/\">AI-Gruppe</a> 集团的成员。", footer_blog="技术博客：<a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a>",
   copyright="© {y} nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)", cd="企业视觉识别手册（PDF，德文）",
   ref_title="欢迎来到 nabla B。", ref_text="您来自 Stephan Bökelmann 的博客 maxclerkwell.tech。nabla B 是他在波鸿的工程事务所，博客中描述的项目均通过该公司承接。这里有服务、团队、案例与联系方式。", ref_ok="明白了", ref_back="返回博客"),
}
LANGNAME = {"de": ("🇩🇪","DE","Deutsch"), "en": ("🇬🇧","EN","English"), "zh": ("🇨🇳","中文","中文")}
HTMLLANG = {"de":"de","en":"en","zh":"zh-Hans"}

# ---------------------------------------------------------------- page content
def content(lang):
    L = lang
    ref_hdr = {"de":"Referenzen","en":"References","zh":"项目案例"}[L]
    C = {}
    # ---- index
    C["index"] = dict(
      title={"de":"nabla B – Ingenieurbüro für Embedded-Systeme, Messtechnik & DAQ, Bochum",
             "en":"nabla B – Engineering office for embedded systems, measurement & DAQ, Bochum",
             "zh":"nabla B – 嵌入式系统、测量技术与数据采集工程事务所（德国波鸿）"}[L],
      desc={"de":"Design und Entwicklung von Embedded-Geräten: Architektur, PCB-Design, Zertifizierung, Bring-up und Firmware für µC, FPGA und Zynq. Dezentrale Messtechnik & DAQ, Beratung, Schulung. Bochum.",
            "en":"Design and development of embedded devices: architecture, PCB design, certification, bring-up and firmware for MCU, FPGA and Zynq. Decentralised measurement & DAQ, consulting, training. Bochum, Germany.",
            "zh":"嵌入式设备的设计与开发：架构、PCB 设计、认证、启动调试以及 MCU/FPGA/Zynq 固件。分布式测量与数据采集、咨询、培训。德国波鸿。"}[L],
      hero_h1={"de":"Embedded-Geräte.<br>Von der Architektur bis zur Firmware.",
               "en":"Embedded devices.<br>From architecture to firmware.",
               "zh":"嵌入式设备。<br>从架构到固件。"}[L],
      hero_lead={"de":"nabla B ist ein Ingenieurbüro in Bochum. Wir entwickeln Embedded-Geräte und dezentrale Messtechnik für den Mittelstand – und bringen sie in Serie.",
                 "en":"nabla B is an engineering office in Bochum, Germany. We develop embedded devices and decentralised measurement systems for mid-sized industry — and take them to production.",
                 "zh":"nabla B 是位于德国波鸿的工程事务所。我们为中型企业开发嵌入式设备与分布式测量系统——并将其推向量产。"}[L],
      pillars={"de":["Architektur & Systemdesign","PCB-Design & Zertifizierung","Bring-up für µC, FPGA & Zynq","Firmware & Yocto Linux","Dezentrale Messtechnik & DAQ","Beratung & Schulung"],
               "en":["Architecture & system design","PCB design & certification","Bring-up for MCU, FPGA & Zynq","Firmware & Yocto Linux","Decentralised measurement & DAQ","Consulting & training"],
               "zh":["架构与系统设计","PCB 设计与认证","MCU / FPGA / Zynq 启动调试","固件与 Yocto Linux","分布式测量与数据采集","咨询与培训"]}[L],
      cta={"de":"Termin mit Stephan Bökelmann vereinbaren","en":"Book an appointment with Stephan Bökelmann","zh":"预约与 Stephan Bökelmann 交流"}[L],
      cta_note={"de":"Tagessatz ab 80 € netto. Erstgespräch kostenlos – telefonisch Mo – Fr 9:00 – 13:30 Uhr oder per E-Mail.",
                "en":"Day rate from € 80 net. Initial consultation free of charge — by phone Mon – Fri 9:00 – 13:30 CET or by e-mail.",
                "zh":"日费率 80 欧元起（不含税）。首次咨询免费——周一至周五 9:00 – 13:30（中欧时间）电话，或发送电子邮件。"}[L],
      cta_mail_subject={"de":"Terminanfrage","en":"Appointment request","zh":"预约咨询"}[L],
      what_h={"de":"Was wir tun","en":"What we do","zh":"我们做什么"}[L],
      what_intro={"de":"Ein Gerät ist erst fertig, wenn es zertifiziert ist, bootet und im Feld Daten liefert. Wir übernehmen den ganzen Weg oder genau den Abschnitt, der Ihnen fehlt.",
                  "en":"A device is only finished when it is certified, boots, and delivers data in the field. We cover the whole path — or exactly the segment you are missing.",
                  "zh":"一台设备只有通过认证、能够启动并在现场提供数据时才算完成。我们可以承担全流程，也可以只负责您所缺的环节。"}[L],
      cards={"de":[("Embedded-Hardware","Architektur, Schaltplan und Layout in KiCad, Bring-up, EMV-Vorbereitung und Zertifizierung, Übergabe an die Fertigung – inklusive Lieferketten-Erfahrung mit Leiterplatten- und Kabelherstellern in China."),
                   ("Firmware & Bring-up","Software-Bring-up und Firmware für Mikrocontroller (bare-metal, RTOS), FPGA (VHDL/Verilog) und Zynq-SoCs – bis zum Yocto Linux mit dokumentierter SBOM und Update-Pfad."),
                   ("Dezentrale Messtechnik & DAQ","Messintelligenz dorthin, wo die Daten entstehen: Analog-Frontends, Sensorik, PoE-Netze, Zeitbasis, Telemetrie und Monitoring-Infrastruktur."),
                   ("Beratung & Schulung","Feasibility, Architektur-Reviews, Toolchain-Rettung. Schulungen für Ingenieure in digitaler Messtechnik und Datenerfassung – in Ihrem Haus oder online.")],
             "en":[("Embedded hardware","Architecture, schematic and layout in KiCad, bring-up, EMC preparation and certification, handover to manufacturing — including supply-chain experience with PCB and cable manufacturers in China."),
                   ("Firmware & bring-up","Software bring-up and firmware for microcontrollers (bare-metal, RTOS), FPGAs (VHDL/Verilog) and Zynq SoCs — up to a Yocto Linux with documented SBOM and update path."),
                   ("Decentralised measurement & DAQ","Measurement intelligence where the data originates: analog front-ends, sensors, PoE networks, time base, telemetry and monitoring infrastructure."),
                   ("Consulting & training","Feasibility, architecture reviews, toolchain rescue. Training for engineers in digital measurement technology and data acquisition — on site or online.")],
             "zh":[("嵌入式硬件","架构、KiCad 原理图与布局、启动调试、EMC 预处理与认证、移交生产——包括与中国 PCB 及线缆制造商合作的供应链经验。"),
                   ("固件与启动调试","微控制器（裸机、RTOS）、FPGA（VHDL/Verilog）和 Zynq SoC 的软件启动调试与固件——直至带完整 SBOM 与更新路径的 Yocto Linux。"),
                   ("分布式测量与数据采集","把测量智能放在数据产生的地方：模拟前端、传感器、PoE 网络、时基、遥测与监测基础设施。"),
                   ("咨询与培训","可行性研究、架构评审、工具链救援。面向工程师的数字测量技术与数据采集培训——上门或在线。")]}[L],
      refs_h=ref_hdr,
      refs_intro={"de":"Eine Auswahl – die vollständige Liste steht auf der Referenzseite. Vieles, was wir bauen, dürfen wir wegen NDAs nicht zeigen.",
                  "en":"A selection — the full list is on the references page. Much of what we build cannot be shown because of NDAs.",
                  "zh":"精选案例——完整列表见项目案例页。由于保密协议，我们的许多项目无法公开展示。"}[L],
      refs_more={"de":"Alle Referenzen","en":"All references","zh":"全部项目案例"}[L],
      blog_h={"de":"Aus dem Labor","en":"From the lab","zh":"来自实验室"}[L],
      blog_p={"de":"Auf <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a> schreibt Stephan Bökelmann über seine Hobby- und Forschungsprojekte: FPGA-Bring-ups, Yocto, KiCad, Teilchendetektoren. Die Kundenprojekte von nabla B tauchen dort meist nicht auf – die meisten stehen unter NDA. Der Blog zeigt aber gut, wie wir arbeiten.",
              "en":"On <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a> Stephan Bökelmann writes about his hobby and research projects: FPGA bring-ups, Yocto, KiCad, particle detectors. nabla B's customer projects mostly don't appear there — most are under NDA. But the blog shows well how we work.",
              "zh":"Stephan Bökelmann 在 <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a> 上撰写他的业余与科研项目：FPGA 启动调试、Yocto、KiCad、粒子探测器。nabla B 的客户项目大多不会出现在那里——多数受保密协议约束。但博客很好地展示了我们的工作方式。"}[L],
      contact_h={"de":"Sprechen wir über Ihr Gerät","en":"Let's talk about your device","zh":"聊聊您的设备"}[L],
    )
    # ---- leistungen
    C["leistungen"] = dict(
      title={"de":"Leistungen – nabla B Ingenieurbüro","en":"Services – nabla B engineering office","zh":"服务 – nabla B 工程事务所"}[L],
      desc={"de":"Embedded-Hardware, Firmware für µC/FPGA/Zynq, dezentrale Messtechnik & DAQ, Beratung und Schulung. Tagessatz ab 80 € netto.",
            "en":"Embedded hardware, firmware for MCU/FPGA/Zynq, decentralised measurement & DAQ, consulting and training. Day rate from € 80 net.",
            "zh":"嵌入式硬件、MCU/FPGA/Zynq 固件、分布式测量与数据采集、咨询与培训。日费率 80 欧元起。"}[L],
      h1={"de":"Leistungen","en":"Services","zh":"服务"}[L],
      intro={"de":"Design und Entwicklung von Embedded-Geräten – von der Architektur über PCB-Design und Zertifizierung zum Software-Bring-up für µC, FPGA und Zynq bis hin zur Firmware. Dazu dezentrale Messtechnik & DAQ, Beratung und Schulung.",
             "en":"Design and development of embedded devices — from architecture via PCB design and certification to software bring-up for MCU, FPGA and Zynq, all the way to firmware. Plus decentralised measurement & DAQ, consulting and training.",
             "zh":"嵌入式设备的设计与开发——从架构、PCB 设计与认证，到 MCU/FPGA/Zynq 的软件启动调试，直至固件。此外还有分布式测量与数据采集、咨询与培训。"}[L],
      blocks={"de":[
        ("1. Architektur & Systemdesign",["Anforderungsanalyse, Machbarkeit, Blockdiagramm","Auswahl von SoC, µC, FPGA, Sensorik und Schnittstellen","Bus- und Netzwerkkonzepte: Ethernet/PoE, CAN, RS-485, LoRaWAN, USB","Sicherheits- und Update-Konzept von Anfang an"]),
        ("2. PCB-Design",["Schaltplan und Layout in KiCad","Mixed-Signal, Analog-Frontends, Power","Design for Manufacturing, Lieferkette (auch China)","Mechanik-Integration, gehäuselose Bauformen"]),
        ("3. Zertifizierung",["EMV-Vorbereitung und Begleitung im Prüflabor","CE-Konformität, Dokumentation","Erfahrung mit Prüfläufen in Deutschland und China"]),
        ("4. Software-Bring-up",["Mikrocontroller: bare-metal, RTOS, Bootloader","FPGA: VHDL/Verilog, Bitstream-Pipelines","Zynq: FSBL/U-Boot, Devicetree, Yocto Linux mit SBOM","Versionierte, reproduzierbare Toolchains"]),
        ("5. Firmware",["Treiber, Protokolle, Messdatenpfade","Over-the-air-Updates, Telemetrie, Logging","Tests auf Hardware-in-the-Loop-Ständen"]),
        ("6. Dezentrale Messtechnik & DAQ",["Messknoten statt Messrechner: Zeitstempel an der Quelle","Analog-Frontends, Sensorik, PoE-Messnetze","Von Excel-Inseln zu einer gemeinsamen Zeitbasis"]),
        ("7. Monitoring & Observability",["Telemetrie-Pipelines vom Gerät bis ins Dashboard","Condition Monitoring, Predictive Maintenance","Betrieb, Alarmierung, Langzeitarchivierung"]),
        ("8. Beratung",["Machbarkeitsstudien und Second Opinion","Architektur-Reviews bestehender Geräte","Toolchain-Rettung: reproduzierbar statt fragil"]),
        ("9. Schulung",["Digitale Messtechnik und Datenerfassung für Ingenieure","Embedded-Linux, FPGA und KiCad in der Praxis","Inhouse-Workshops oder online"]),
      ],"en":[
        ("1. Architecture & system design",["Requirements, feasibility, block diagram","Selection of SoC, MCU, FPGA, sensors and interfaces","Bus and network concepts: Ethernet/PoE, CAN, RS-485, LoRaWAN, USB","Security and update concept from day one"]),
        ("2. PCB design",["Schematic and layout in KiCad","Mixed-signal, analog front-ends, power","Design for manufacturing, supply chain (incl. China)","Mechanical integration, enclosureless designs"]),
        ("3. Certification",["EMC preparation and support in the test lab","CE conformity, documentation","Experience with test runs in Germany and China"]),
        ("4. Software bring-up",["Microcontrollers: bare-metal, RTOS, bootloaders","FPGA: VHDL/Verilog, bitstream pipelines","Zynq: FSBL/U-Boot, device tree, Yocto Linux with SBOM","Versioned, reproducible toolchains"]),
        ("5. Firmware",["Drivers, protocols, measurement data paths","Over-the-air updates, telemetry, logging","Testing on hardware-in-the-loop rigs"]),
        ("6. Decentralised measurement & DAQ",["Measurement nodes instead of measurement PCs: timestamps at the source","Analog front-ends, sensors, PoE measurement networks","From Excel islands to a shared time base"]),
        ("7. Monitoring & observability",["Telemetry pipelines from device to dashboard","Condition monitoring, predictive maintenance","Operations, alerting, long-term archiving"]),
        ("8. Consulting",["Feasibility studies and second opinion","Architecture reviews of existing devices","Toolchain rescue: reproducible instead of fragile"]),
        ("9. Training",["Digital measurement technology and DAQ for engineers","Embedded Linux, FPGA and KiCad in practice","In-house workshops or online"]),
      ],"zh":[
        ("1. 架构与系统设计",["需求分析、可行性、框图","SoC、MCU、FPGA、传感器与接口选型","总线与网络方案：Ethernet/PoE、CAN、RS-485、LoRaWAN、USB","从第一天起的安全与更新方案"]),
        ("2. PCB 设计",["KiCad 原理图与布局","混合信号、模拟前端、电源","可制造性设计、供应链（含中国）","机械集成、无外壳结构"]),
        ("3. 认证",["EMC 预处理及实验室测试陪同","CE 符合性、文档","在德国与中国进行测试的经验"]),
        ("4. 软件启动调试",["微控制器：裸机、RTOS、引导加载程序","FPGA：VHDL/Verilog、比特流流水线","Zynq：FSBL/U-Boot、设备树、带 SBOM 的 Yocto Linux","版本化、可复现的工具链"]),
        ("5. 固件",["驱动、协议、测量数据通路","OTA 更新、遥测、日志","硬件在环测试台上的测试"]),
        ("6. 分布式测量与数据采集",["用测量节点取代测量电脑：在数据源打时间戳","模拟前端、传感器、PoE 测量网络","从 Excel 孤岛到统一时基"]),
        ("7. 监测与可观测性",["从设备到仪表盘的遥测管线","状态监测、预测性维护","运维、告警、长期归档"]),
        ("8. 咨询",["可行性研究与第二意见","现有设备的架构评审","工具链救援：可复现而非脆弱"]),
        ("9. 培训",["面向工程师的数字测量技术与数据采集","嵌入式 Linux、FPGA 与 KiCad 实践","企业内训或在线"]),
      ]}[L],
      pricing_h={"de":"Konditionen","en":"Terms","zh":"合作条款"}[L],
      pricing={"de":"Tagessatz ab 80 € netto, abhängig von Aufgabe und Laufzeit. Festpreise für klar umrissene Pakete (z. B. Machbarkeitsstudie, PCB-Layout, Schulungstag) auf Anfrage. Vertragspartner ist die nabla B UG; bei Bedarf holen wir Kapazität aus der AI-Gruppe dazu – Vertrag und Verantwortung bleiben bei nabla B.",
               "en":"Day rate from € 80 net, depending on task and duration. Fixed prices for clearly scoped packages (e.g. feasibility study, PCB layout, training day) on request. Your contracting party is nabla B UG; when a project needs it we add capacity from the AI-Gruppe — contract and responsibility stay with nabla B.",
               "zh":"日费率 80 欧元起（不含税），视任务与周期而定。范围明确的项目包（如可行性研究、PCB 布局、培训日）可按需报固定价。签约方为 nabla B UG；需要时我们会从 AI-Gruppe 调配产能——合同与责任始终由 nabla B 承担。"}[L],
      cta={"de":"Termin mit Stephan Bökelmann vereinbaren","en":"Book an appointment with Stephan Bökelmann","zh":"预约与 Stephan Bökelmann 交流"}[L],
    )
    # ---- referenzen
    C["referenzen"] = dict(
      title={"de":"Referenzen – nabla B","en":"References – nabla B","zh":"项目案例 – nabla B"}[L],
      desc={"de":"Ausgewählte Projekte von nabla B und Stephan Bökelmann: skAInet Edge-Compute, Reflow-Monitoring, OmnAIScope, HV-MAPS-Teststände, Zynq-Pipelines.",
            "en":"Selected projects by nabla B and Stephan Bökelmann: skAInet Edge-Compute, reflow monitoring, OmnAIScope, HV-MAPS test stands, Zynq pipelines.",
            "zh":"nabla B 与 Stephan Bökelmann 的精选项目：skAInet Edge-Compute、回流焊监测、OmnAIScope、HV-MAPS 测试台、Zynq 流水线。"}[L],
      h1=ref_hdr,
      intro={"de":"Projekte aus Industrie und Forschung, an denen nabla B bzw. Stephan Bökelmann maßgeblich beteiligt war oder ist. Viele Kundenprojekte stehen unter NDA und fehlen hier – sprechen Sie uns an, wenn Sie Referenzen aus Ihrer Branche brauchen.",
             "en":"Projects from industry and research in which nabla B or Stephan Bökelmann played or plays a major role. Many customer projects are under NDA and are missing here — ask us if you need references from your industry.",
             "zh":"nabla B 或 Stephan Bökelmann 主导或深度参与的工业与科研项目。许多客户项目受保密协议约束未在此列出——如需您所在行业的参考案例，请与我们联系。"}[L],
      note={"de":"<strong>Hinweis:</strong> Das <a href=\"https://edge-compute.skainet.io/\">skAInet Edge-Compute</a> ist ein Produkt der Auto-Intern GmbH; nabla B ist als Systemarchitekt beteiligt. Mehr zu unseren Hobby- und Forschungsprojekten auf <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a>.",
            "en":"<strong>Note:</strong> The <a href=\"https://edge-compute.skainet.io/\">skAInet Edge-Compute</a> is a product of Auto-Intern GmbH; nabla B contributes as system architect. More on our hobby and research projects at <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a>.",
            "zh":"<strong>说明：</strong><a href=\"https://edge-compute.skainet.io/\">skAInet Edge-Compute</a> 是 Auto-Intern GmbH 的产品；nabla B 以系统架构师身份参与。更多业余与科研项目见 <a href=\"https://maxclerkwell.tech/\">maxclerkwell.tech</a>。"}[L],
    )
    # ---- team
    C["team"] = dict(
      title={"de":"Team – nabla B","en":"Team – nabla B","zh":"团队 – nabla B"}[L],
      desc={"de":"Das Team von nabla B in Bochum: Stephan Bökelmann, Tabea Bökelmann, Meihui Huang, Vanessa Wilcken, Atiyeh Chatrsefid.",
            "en":"The nabla B team in Bochum: Stephan Bökelmann, Tabea Bökelmann, Meihui Huang, Vanessa Wilcken, Atiyeh Chatrsefid.",
            "zh":"nabla B 波鸿团队：Stephan Bökelmann、Tabea Bökelmann、Meihui Huang、Vanessa Wilcken、Atiyeh Chatrsefid。"}[L],
      h1={"de":"Team","en":"Team","zh":"团队"}[L],
      intro={"de":"Klein, technisch, direkt erreichbar. Sie sprechen mit den Leuten, die Ihr Gerät bauen.",
             "en":"Small, technical, directly reachable. You talk to the people who build your device.",
             "zh":"团队精悍、技术导向、直接可联系。与您沟通的就是为您打造设备的人。"}[L],
      disambig={"de":"Stephan Bökelmann (auch: Stephan Boekelmann, MaxClerkwell, 施泓杰) — nicht ClerksWell, nicht der Schauspieler Stefan Bockelmann.",
                "en":"Stephan Bökelmann (also: Stephan Boekelmann, MaxClerkwell, 施泓杰) — not ClerksWell, not the actor Stefan Bockelmann.",
                "zh":"施泓杰（Stephan Bökelmann，又名 Stephan Boekelmann、MaxClerkwell）——与 ClerksWell 及演员 Stefan Bockelmann 无关。"}[L],
      people=[
        dict(id="stephan-boekelmann", pid=PERSON_STEPHAN, name="Stephan Bökelmann", img="/assets/img/stephan-boekelmann.jpg",
             short={"de":"Ingenieur und Physiker, seit 2007 im Beruf. Systemarchitekt des skAInet Edge-Compute, Promotion in Hadronenphysik (PANDA/FAIR), Dozent an THGA und RUB.",
                    "en":"Engineer and physicist, professionally active since 2007. System architect of the skAInet Edge-Compute, PhD in hadron physics (PANDA/FAIR), lecturer at THGA and RUB.",
                    "zh":"工程师与物理学家，2007 年起从业。skAInet Edge-Compute 系统架构师，强子物理博士研究（PANDA/FAIR），THGA 与波鸿鲁尔大学讲师。"}[L],
             edu_short={"de":["B.Eng. Elektrotechnik · M.Eng. Technische Informatik (THGA)","Promotion Hadronenphysik (RUB, laufend)"],"en":["B.Eng. EE · M.Eng. Computer Engineering (THGA)","PhD hadron physics (RUB, ongoing)"],"zh":["电气工学学士 · 计算机工程硕士（THGA）","强子物理博士（RUB，在读）"]}[L],
             role={"de":"Geschäftsführender Gesellschafter · Ingenieur & Physiker","en":"Managing Director · Engineer & Physicist","zh":"执行合伙人 · 工程师与物理学家"}[L],
             bio={"de":"Seit 2007 im Beruf, vom Mechaniker und Elektroniker über B.Eng. und M.Eng. bis zur Promotion in experimenteller Hadronenphysik (PANDA/FAIR). Systemarchitekt des skAInet Edge-Compute, Dozent an THGA und RUB, Organisator von emBO++ und KiCon Europe.",
                  "en":"Professionally active since 2007, from mechanic and electrician via B.Eng. and M.Eng. to a PhD in experimental hadron physics (PANDA/FAIR). System architect of the skAInet Edge-Compute, lecturer at THGA and RUB, organiser of emBO++ and KiCon Europe.",
                  "zh":"2007 年起从业，从机械工与电工，到工学学士、硕士，再到实验强子物理博士研究（PANDA/FAIR）。skAInet Edge-Compute 系统架构师，THGA 与波鸿鲁尔大学讲师，emBO++ 与 KiCon Europe 组织者。"}[L],
             edu={"de":["B.Eng. Elektro- und Informationstechnik, THGA Bochum","M.Eng. Informationstechnik / Technische Informatik, THGA Bochum","Promotion (laufend) Experimentelle Hadronenphysik, Ruhr-Universität Bochum"],
                  "en":["B.Eng. Electrical and Information Technology, THGA Bochum","M.Eng. Information Technology / Computer Engineering, THGA Bochum","PhD (ongoing) Experimental Hadron Physics, Ruhr-Universität Bochum"],
                  "zh":["电气与信息技术工学学士，THGA 波鸿","信息技术/计算机工程工学硕士，THGA 波鸿","实验强子物理博士（在读），波鸿鲁尔大学"]}[L],
             links=[("maxclerkwell.tech","https://maxclerkwell.tech/"),("LinkedIn","https://www.linkedin.com/in/accelerator-stephan/"),("GitHub","https://github.com/maxclerkwell"),("ORCID","https://orcid.org/0000-0002-2119-0064")],
             jobTitle=["Managing Director, nabla B","Chief Operating Officer, Auto-Intern GmbH","System Architect, skAInet Edge-Compute"], alt=["MaxClerkwell","Stephan Boekelmann","施泓杰"],
             sameAs=["https://www.linkedin.com/in/accelerator-stephan/","https://github.com/maxclerkwell","https://orcid.org/0000-0002-2119-0064",
                     "https://x.com/maxclerkwell","https://instagram.com/_maxclerkwell","https://www.researchgate.net/profile/Stephan-Boekelmann",
                     "https://inspirehep.net/authors/2177110","https://www.thga.de/hochschule/personen/profile-wissenschaftliche-mitarbeitende/stephan-boekelmann",
                     "https://edge-compute.skainet.io/team#stephan-boekelmann"],
             knows=["embedded systems","FPGA","Zynq","PCB design","KiCad","data acquisition","Yocto Linux","experimental hadron physics"],
             creds=[("bachelor degree","B.Eng. Electrical and Information Technology"),("master degree","M.Eng. Information Technology / Computer Engineering")],
             alumni=[("THGA Bochum","https://www.thga.de/"),("Ruhr-Universität Bochum","https://www.ruhr-uni-bochum.de/")]),
        dict(id="tabea-boekelmann", pid=PERSON_TABEA, name="Tabea Bökelmann", img="/assets/img/tabea-boekelmann.jpg",
             short={"de":"Physikerin und Informatikerin. Baut die Frontends von nabla B – von Messdaten-Dashboards bis zur Bedienoberfläche eingebetteter Geräte.",
                    "en":"Physicist and computer scientist. Builds nabla B's frontends — from measurement-data dashboards to embedded device UIs.",
                    "zh":"物理学家与计算机科学家。负责 nabla B 的前端——从测量数据仪表盘到嵌入式设备界面。"}[L],
             edu_short={"de":["B.Sc. Physik · B.Sc. Angewandte Informatik (RUB)","M.Sc. Angewandte Informatik – „Git with Features“ (RUB)"],"en":["B.Sc. Physics · B.Sc. Applied CS (RUB)","M.Sc. Applied CS – “Git with Features” (RUB)"],"zh":["物理学学士 · 应用计算机科学学士（RUB）","应用计算机科学硕士 –《Git with Features》（RUB）"]}[L],
             role={"de":"Senior Frontend Consultant · Angular & JavaScript","en":"Senior Frontend Consultant · Angular & JavaScript","zh":"高级前端顾问 · Angular 与 JavaScript"}[L],
             bio={"de":"Physikerin und Informatikerin. Verantwortet bei nabla B die Frontends – von Dashboards für Messdaten bis zur Bedienoberfläche eingebetteter Geräte. Masterarbeit „Git with Features“ (Software-Engineering); Bachelor in Teilchenphysik (Hadronenphysik, DAQ) und in eingebetteten Systemen (RISC-V, Compilerbau).",
                  "en":"Physicist and computer scientist. Responsible for nabla B's frontends — from measurement-data dashboards to the user interface of embedded devices. Master's thesis “Git with Features” (software engineering); bachelor's degrees in particle physics (hadron physics, DAQ) and in embedded systems (RISC-V, compiler construction).",
                  "zh":"物理学家与计算机科学家。负责 nabla B 的前端——从测量数据仪表盘到嵌入式设备的用户界面。硕士论文《Git with Features》（软件工程）；粒子物理（强子物理、数据采集）与嵌入式系统（RISC-V、编译器）双学士。"}[L],
             edu={"de":["B.Sc. Physik – Teilchenphysik, Hadronenphysik, DAQ, Ruhr-Universität Bochum","B.Sc. Angewandte Informatik – eingebettete Systeme, RISC-V, Compiler, Ruhr-Universität Bochum","M.Sc. Angewandte Informatik – „Git with Features“, Software-Engineering, Ruhr-Universität Bochum"],
                  "en":["B.Sc. Physics – particle physics, hadron physics, DAQ, Ruhr-Universität Bochum","B.Sc. Applied Computer Science – embedded systems, RISC-V, compilers, Ruhr-Universität Bochum","M.Sc. Applied Computer Science – “Git with Features”, software engineering, Ruhr-Universität Bochum"],
                  "zh":["物理学学士 – 粒子物理、强子物理、数据采集，波鸿鲁尔大学","应用计算机科学学士 – 嵌入式系统、RISC-V、编译器，波鸿鲁尔大学","应用计算机科学硕士 – 《Git with Features》、软件工程，波鸿鲁尔大学"]}[L],
             links=[("LinkedIn","https://www.linkedin.com/in/tabea-b%C3%B6kelmann-0b9794198/"),("ResearchGate","https://www.researchgate.net/profile/Tabea-Roethemeyer"),("YouTube","https://www.youtube.com/watch?v=DgHCycO6ohs")],
             jobTitle="Senior Frontend Consultant", alt=["Tabea Viktoria Bökelmann","Tabea Boekelmann","Tabea Böckelmann","Tabea Boeckelmann","Tabea Bockelmann","Tabea Röthemeyer"],
             sameAs=["https://www.linkedin.com/in/tabea-b%C3%B6kelmann-0b9794198/","https://www.researchgate.net/profile/Tabea-Roethemeyer","https://www.youtube.com/watch?v=DgHCycO6ohs","https://edge-compute.skainet.io/team"],
             knows=["Angular","JavaScript","TypeScript","frontend architecture","software engineering","Git","embedded systems","RISC-V","compiler construction","particle physics","data acquisition"],
             creds=[("bachelor degree","B.Sc. Physics"),("bachelor degree","B.Sc. Applied Computer Science"),("master degree","M.Sc. Applied Computer Science")],
             alumni=[("Ruhr-Universität Bochum","https://www.ruhr-uni-bochum.de/")]),
        dict(id="meihui-huang", pid=PERSON_MEIHUI, name="Meihui Huang", img="/assets/img/meihui-huang.jpg",
             short={"de":"Physikerin aus Tianjin. Unterstützt Messaufbauten, Detektortests und Auswertung; betreut die Social-Media-Kanäle von maxclerkwell.tech.",
                    "en":"Physicist from Tianjin. Supports measurement setups, detector tests and analysis; runs the maxclerkwell.tech social media channels.",
                    "zh":"来自天津的物理学家。负责测量装置、探测器测试与数据分析；运营 maxclerkwell.tech 的社交媒体。"}[L],
             edu_short={"de":["B.Sc. Physik, Nankai-Universität Tianjin","M.Sc. Physik, RUB EP1 – AG Hadronen und Kerne (laufend)"],"en":["B.Sc. Physics, Nankai University Tianjin","M.Sc. Physics, RUB EP1 – Hadrons and Nuclei (ongoing)"],"zh":["物理学学士，南开大学（天津）","物理学硕士，RUB EP1 强子与原子核组（在读）"]}[L],
             role={"de":"Physikerin · Werkstudentin · Research und Outreach","en":"Physicist · Working student · Research and Outreach","zh":"物理学家 · 在读实习生 · 科研与推广"}[L],
             bio={"de":"Physikerin aus Tianjin, lebt in Witten. B.Sc. Physik (Teilchenphysik) an der Nankai-Universität mit Zerfallsketten-Analyse in ROOT; M.Sc.-Studentin an der Ruhr-Universität Bochum, Institut für Experimentalphysik I, AG Hadronen und Kerne. Unterstützt Messaufbauten, Detektortests und Auswertung – und betreut als Social Media Executive die Kanäle von maxclerkwell.tech.",
                  "en":"Physicist from Tianjin, based in Witten. B.Sc. Physics (particle physics) at Nankai University with decay-chain analysis in ROOT; M.Sc. student at Ruhr-Universität Bochum, Institute for Experimental Physics I, Hadrons and Nuclei group. Supports measurement setups, detector tests and analysis — and runs the maxclerkwell.tech channels as social media executive.",
                  "zh":"来自天津的物理学家，现居维滕。南开大学物理学学士（粒子物理），用 ROOT 进行衰变链分析；波鸿鲁尔大学实验物理研究所 I 强子与原子核研究组硕士生。负责测量装置搭建、探测器测试与数据分析，并作为社交媒体运营负责 maxclerkwell.tech 的各个频道。"}[L],
             edu={"de":["B.Sc. Physik – Teilchenphysik, Zerfallsketten-Analyse mit ROOT, Nankai-Universität Tianjin","M.Sc. Physik (laufend) – Experimentalphysik I, AG Hadronen und Kerne, Ruhr-Universität Bochum"],
                  "en":["B.Sc. Physics – particle physics, decay-chain analysis with ROOT, Nankai University, Tianjin","M.Sc. Physics (ongoing) – Experimental Physics I, Hadrons and Nuclei group, Ruhr-Universität Bochum"],
                  "zh":["物理学学士 – 粒子物理、ROOT 衰变链分析，南开大学（天津）","物理学硕士（在读）– 实验物理 I，强子与原子核研究组，波鸿鲁尔大学"]}[L],
             links=[("LinkedIn","https://www.linkedin.com/in/meihui-huang/"),("ResearchGate","https://www.researchgate.net/profile/Meihui-Huang")],
             jobTitle=["Physicist","Working Student – Research and Outreach"], alt=["Huang Meihui","Huang Mei Hui","黄美慧"],
             sameAs=["https://www.linkedin.com/in/meihui-huang/","https://www.researchgate.net/profile/Meihui-Huang"],
             knows=["particle physics","ROOT","decay chain analysis","detector testing","social media management"],
             creds=[("bachelor degree","B.Sc. Physics")],
             alumni=[("Nankai University","https://www.nankai.edu.cn/"),("Ruhr-Universität Bochum","https://www.ruhr-uni-bochum.de/")]),
        dict(id="vanessa-wilcken", pid=PERSON_VANESSA, name="Vanessa Wilcken", img="/assets/img/vanessa-wilcken.jpg",
             short={"de":"Ihre erste Ansprechpartnerin: Termine, Angebote, Rechnungen. Mo – Fr 9:00 – 13:30 Uhr.",
                    "en":"Your first point of contact: appointments, quotes, invoices. Mon – Fri 9:00 – 13:30 CET.",
                    "zh":"您的首要联系人：预约、报价、发票。周一至周五 9:00 – 13:30。"}[L],
             edu_short=[],
             role={"de":"Assistenz der Geschäftsführung · Office","en":"Executive Assistant · Office","zh":"总经理助理 · 办公室"}[L],
             bio={"de":"Ihre erste Ansprechpartnerin: Terminvereinbarung, Angebote, Rechnungen und alles Organisatorische. Erreichbar Mo – Fr 9:00 – 13:30 Uhr.",
                  "en":"Your first point of contact: appointments, quotes, invoices and everything organisational. Available Mon – Fri 9:00 – 13:30 CET.",
                  "zh":"您的首要联系人：预约、报价、发票及所有行政事务。周一至周五 9:00 – 13:30（中欧时间）。"}[L],
             edu=[],
             links=[("LinkedIn","https://www.linkedin.com/in/vanessa-wilcken-1436b320a/"),("office@nabla-b.engineering","mailto:"+MAIL),(TEL,TEL_HREF)],
             jobTitle="Executive Assistant", alt=[], sameAs=["https://www.linkedin.com/in/vanessa-wilcken-1436b320a/"], knows=[], creds=[], alumni=[]),
        dict(id="atiyeh-chatrsefid", pid=PERSON_ATIYEH, name="Atiyeh Chatrsefid", img="/assets/img/atiyeh-chatrsefid.jpg",
             short={"de":"Verantwortlich für Business Development: neue Kunden, Partnerschaften und Angebote. MBA in Artificial Intelligence, Informatik an der RUB.",
                    "en":"Responsible for business development: new customers, partnerships and proposals. MBA in Artificial Intelligence, computer science at RUB.",
                    "zh":"负责业务拓展：新客户、合作伙伴与报价。人工智能 MBA，波鸿鲁尔大学计算机科学。"}[L],
             edu_short={"de":["MBA Artificial Intelligence, Brand University of Applied Sciences","Informatik, Ruhr-Universität Bochum"],"en":["MBA Artificial Intelligence, Brand University of Applied Sciences","Computer Science, Ruhr-Universität Bochum"],"zh":["人工智能 MBA，Brand University of Applied Sciences","计算机科学，波鸿鲁尔大学"]}[L],
             role={"de":"Business Development · MBA in AI","en":"Business Development · MBA in AI","zh":"业务拓展 · 人工智能 MBA"}[L],
             bio={"de":"Verantwortet bei nabla B das Business Development – Kundenakquise, Partnerschaften und Angebotsentwicklung. MBA in Artificial Intelligence (Brand University of Applied Sciences), Informatikstudium an der Ruhr-Universität Bochum. Zuvor Commercial Lead beim KI-Start-up Wisdom Bridge AI, KI-Strategieberaterin für den Mittelstand und Praktikantin im Projektmanagement bei Deloitte. Registered Product Owner (Scrum Inc.).",
                  "en":"Responsible for business development at nabla B — customer acquisition, partnerships and proposal development. MBA in Artificial Intelligence (Brand University of Applied Sciences), computer science studies at Ruhr-Universität Bochum. Previously commercial lead at the AI start-up Wisdom Bridge AI, AI strategy consultant for mid-sized companies and project management intern at Deloitte. Registered Product Owner (Scrum Inc.).",
                  "zh":"负责 nabla B 的业务拓展——客户开发、合作伙伴关系与方案报价。人工智能 MBA（Brand University of Applied Sciences），波鸿鲁尔大学计算机科学。此前任 AI 初创公司 Wisdom Bridge AI 商务负责人、中小企业 AI 战略顾问，并在德勤从事项目管理实习。Registered Product Owner（Scrum Inc.）。"}[L],
             edu={"de":["MBA – Artificial Intelligence, Brand University of Applied Sciences, Hamburg","Informatik, Ruhr-Universität Bochum"],
                  "en":["MBA – Artificial Intelligence, Brand University of Applied Sciences, Hamburg","Computer Science, Ruhr-Universität Bochum"],
                  "zh":["MBA – 人工智能，Brand University of Applied Sciences（汉堡）","计算机科学，波鸿鲁尔大学"]}[L],
             links=[("LinkedIn","https://www.linkedin.com/in/atiyeh-chatrsefid-/"),(MAIL_ATIYEH,"mailto:"+MAIL_ATIYEH)],
             jobTitle="Business Development", alt=[], sameAs=["https://www.linkedin.com/in/atiyeh-chatrsefid-/"],
             knows=["business development","AI strategy","startup strategy","product ownership","IT consulting"],
             creds=[("master degree","MBA Artificial Intelligence")],
             alumni=[("Brand University of Applied Sciences","https://www.brand-university.de/"),("Ruhr-Universität Bochum","https://www.ruhr-uni-bochum.de/")]),
      ],
    )
    # ---- kontakt
    C["kontakt"] = dict(
      title={"de":"Kontakt – nabla B, Bochum","en":"Contact – nabla B, Bochum","zh":"联系 – nabla B（波鸿）"}[L],
      desc={"de":"nabla B Ingenieurbüro, Herner Str. 299, Gebäude B29, 44809 Bochum. Telefon +49 234 58545811, office@nabla-b.engineering. Mo – Fr 9:00 – 13:30 Uhr.",
            "en":"nabla B engineering office, Herner Str. 299, Building B29, 44809 Bochum, Germany. Phone +49 234 58545811, office@nabla-b.engineering. Mon – Fri 9:00 – 13:30 CET.",
            "zh":"nabla B 工程事务所，Herner Str. 299, Gebäude B29, 44809 Bochum，德国。电话 +49 234 58545811，office@nabla-b.engineering。周一至周五 9:00 – 13:30。"}[L],
      h1={"de":"Kontakt","en":"Contact","zh":"联系我们"}[L],
      intro={"de":"Ihre Ansprechpartnerin ist <strong>Vanessa Wilcken</strong>. Sie vereinbart den Termin mit Stephan Bökelmann und kümmert sich um alles Organisatorische.",
             "en":"Your contact is <strong>Vanessa Wilcken</strong>. She arranges your appointment with Stephan Bökelmann and takes care of everything organisational.",
             "zh":"您的联系人是 <strong>Vanessa Wilcken</strong>。她将为您安排与 Stephan Bökelmann 的会谈，并处理所有行政事务。"}[L],
      mail_h={"de":"E-Mail","en":"E-mail","zh":"电子邮件"}[L], tel_h={"de":"Telefon","en":"Phone","zh":"电话"}[L],
      hours_h={"de":"Bürozeiten","en":"Office hours","zh":"办公时间"}[L],
      hours={"de":"Montag – Freitag<br>9:00 – 13:30 Uhr","en":"Monday – Friday<br>9:00 – 13:30 CET","zh":"周一至周五<br>9:00 – 13:30（中欧时间）"}[L],
      addr_h={"de":"Anschrift","en":"Address","zh":"地址"}[L],
      addr="nabla B Ingenieurbüro und Dienstleistungs-UG<br>(haftungsbeschränkt)<br>Herner Str. 299, Gebäude B29<br>44809 Bochum<br>"+{"de":"Deutschland","en":"Germany","zh":"德国"}[L],
      cta={"de":"Terminanfrage per E-Mail","en":"Request an appointment by e-mail","zh":"通过电子邮件预约"}[L],
      cta_mail_subject={"de":"Terminanfrage","en":"Appointment request","zh":"预约咨询"}[L],
      map_h={"de":"Anfahrt","en":"Directions","zh":"路线"}[L],
      map_p={"de":"Gebäude B29 auf dem Gelände Herner Str. 299 (ehemalige Zeche Constantin), Bochum-Riemke. Parkplätze vor Ort; ÖPNV: Stadtbahn U35, Haltestelle „Zeche Constantin“.",
             "en":"Building B29 on the Herner Str. 299 site (former Constantin colliery), Bochum-Riemke. Parking on site; public transport: light rail U35, stop “Zeche Constantin”.",
             "zh":"位于 Herner Str. 299 园区（原 Constantin 煤矿）B29 楼，波鸿 Riemke 区。园区内可停车；公共交通：轻轨 U35，Zeche Constantin 站。"}[L],
      map_link="https://www.openstreetmap.org/search?query=Herner%20Str.%20299%2C%2044809%20Bochum",
    )
    # ---- impressum
    C["impressum"] = dict(
      title={"de":"Impressum – nabla B","en":"Imprint – nabla B","zh":"法律声明 – nabla B"}[L],
      desc={"de":"Impressum der nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt), Bochum, HRB 18817.",
            "en":"Legal notice of nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt), Bochum, HRB 18817.",
            "zh":"nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt) 法律声明，波鸿，HRB 18817。"}[L],
      h1={"de":"Impressum","en":"Imprint (Impressum)","zh":"法律声明（Impressum）"}[L],
      body={"de":f"""
<h2>Angaben gemäß § 5 DDG</h2>
<p>nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)<br>Herner Str. 299, Gebäude B29<br>44809 Bochum<br>Deutschland</p>
<p><strong>Vertreten durch:</strong> Stephan Bökelmann, Geschäftsführer</p>
<h2>Kontakt</h2>
<p>Telefon: <a href="{TEL_HREF}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Registereintrag</h2>
<p>Eintragung im Handelsregister.<br>Registergericht: Amtsgericht Bochum<br>Registernummer: HRB 18817</p>
<h2>Umsatzsteuer-ID</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE338747475</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>Stephan Bökelmann, Anschrift wie oben.</p>
<h2>EU-Streitschlichtung</h2>
<p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener">https://ec.europa.eu/consumers/odr/</a>. Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte und Links</h2>
<p>Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Für Inhalte externer Links sind ausschließlich deren Betreiber verantwortlich; zum Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar.</p>
<h2>Unternehmensgruppe</h2>
<p>nabla B ist Teil der Dachmarke <a href="https://gruppe.ai/">AI-Gruppe</a> (Bochum). Weitere Angaben zu Stephan Bökelmann finden Sie auf <a href="https://maxclerkwell.tech/imprint/">maxclerkwell.tech</a>.</p>
""","en":f"""
<h2>Information pursuant to § 5 DDG (German Digital Services Act)</h2>
<p>nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)<br>Herner Str. 299, Building B29<br>44809 Bochum<br>Germany</p>
<p><strong>Represented by:</strong> Stephan Bökelmann, Managing Director</p>
<h2>Contact</h2>
<p>Phone: <a href="{TEL_HREF}">{TEL}</a><br>E-mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Commercial register</h2>
<p>Register court: Amtsgericht Bochum (local court)<br>Registration number: HRB 18817</p>
<h2>VAT ID</h2>
<p>VAT identification number pursuant to § 27a UStG: DE338747475</p>
<h2>Responsible for content pursuant to § 18 (2) MStV</h2>
<p>Stephan Bökelmann, address as above.</p>
<h2>EU dispute resolution</h2>
<p>The European Commission provides a platform for online dispute resolution: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener">https://ec.europa.eu/consumers/odr/</a>. We are neither willing nor obliged to participate in dispute-resolution proceedings before a consumer arbitration board.</p>
<h2>Liability for content and links</h2>
<p>The contents of these pages were created with the greatest care; we cannot, however, guarantee their accuracy, completeness or timeliness. The operators of external links are solely responsible for their content; no legal violations were apparent at the time of linking.</p>
<h2>Group</h2>
<p>nabla B is part of the <a href="https://gruppe.ai/">AI-Gruppe</a> umbrella brand (Bochum). Further information about Stephan Bökelmann at <a href="https://maxclerkwell.tech/imprint/">maxclerkwell.tech</a>.</p>
<p><em>This English version is provided for convenience; the German version is legally binding.</em></p>
""","zh":f"""
<h2>依据德国《数字服务法》第 5 条（§ 5 DDG）的信息</h2>
<p>nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)<br>Herner Str. 299, Gebäude B29<br>44809 Bochum<br>德国</p>
<p><strong>法定代表：</strong>Stephan Bökelmann，总经理</p>
<h2>联系方式</h2>
<p>电话：<a href="{TEL_HREF}">{TEL}</a><br>电子邮件：<a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>商业登记</h2>
<p>登记法院：波鸿地方法院（Amtsgericht Bochum）<br>登记号：HRB 18817</p>
<h2>增值税识别号</h2>
<p>依据德国《增值税法》第 27a 条：DE338747475</p>
<h2>内容责任人（§ 18 (2) MStV）</h2>
<p>Stephan Bökelmann，地址同上。</p>
<h2>欧盟争议解决</h2>
<p>欧盟委员会提供在线争议解决平台：<a href="https://ec.europa.eu/consumers/odr/" rel="noopener">https://ec.europa.eu/consumers/odr/</a>。我们不愿意也无义务参与消费者仲裁机构的争议解决程序。</p>
<h2>集团</h2>
<p>nabla B 是 <a href="https://gruppe.ai/">AI-Gruppe</a>（波鸿）的成员。关于 Stephan Bökelmann 的更多信息见 <a href="https://maxclerkwell.tech/imprint/">maxclerkwell.tech</a>。</p>
<p><em>本中文版本仅供参考；以德文版本为准。</em></p>
"""}[L],
    )
    # ---- datenschutz
    C["datenschutz"] = dict(
      title={"de":"Datenschutzerklärung – nabla B","en":"Privacy policy – nabla B","zh":"隐私政策 – nabla B"}[L],
      desc={"de":"Datenschutzerklärung für nabla-b.engineering: keine Cookies, kein Tracking, Hosting bei GitHub Pages.",
            "en":"Privacy policy for nabla-b.engineering: no cookies, no tracking, hosted on GitHub Pages.",
            "zh":"nabla-b.engineering 隐私政策：无 Cookie、无跟踪，托管于 GitHub Pages。"}[L],
      h1={"de":"Datenschutzerklärung","en":"Privacy policy","zh":"隐私政策"}[L],
      body={"de":f"""
<p>Diese Website kommt ohne Cookies, ohne Tracking und ohne eingebundene Dienste Dritter aus. Schriften und Bilder werden von dieser Domain ausgeliefert.</p>
<h2>1. Verantwortlicher</h2>
<p>nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt), Herner Str. 299, Gebäude B29, 44809 Bochum. Telefon <a href="{TEL_HREF}">{TEL}</a>, E-Mail <a href="mailto:{MAIL}">{MAIL}</a>. Vertreten durch Stephan Bökelmann.</p>
<h2>2. Hosting (GitHub Pages)</h2>
<p>Diese Website wird bei GitHub Pages gehostet, einem Dienst der GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite verarbeitet GitHub technisch notwendige Daten (IP-Adresse, Zeitpunkt, aufgerufene Seite, User-Agent) in Server-Logfiles, um die Seite auszuliefern und die Sicherheit zu gewährleisten. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren und effizienten Betrieb der Website (Art. 6 Abs. 1 lit. f DSGVO). GitHub ist unter dem EU-US Data Privacy Framework zertifiziert. Weitere Informationen: <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<h2>3. Kontaktaufnahme</h2>
<p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten wir Ihre Angaben zur Bearbeitung der Anfrage und für Anschlussfragen (Art. 6 Abs. 1 lit. b DSGVO bei vorvertraglichen Maßnahmen, sonst lit. f). Die Daten werden gelöscht, sobald sie für den Zweck nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>
<h2>4. Externe Links</h2>
<p>Diese Seite verlinkt auf externe Angebote (z. B. maxclerkwell.tech, skainet.io, LinkedIn, GitHub, OpenStreetMap). Beim Klick gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
<h2>5. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Sie können sich bei einer Datenschutz-Aufsichtsbehörde beschweren; für uns zuständig ist die Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen.</p>
<p>Stand: {TODAY}</p>
""","en":f"""
<p>This website uses no cookies, no tracking and no embedded third-party services. Fonts and images are served from this domain.</p>
<h2>1. Controller</h2>
<p>nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt), Herner Str. 299, Building B29, 44809 Bochum, Germany. Phone <a href="{TEL_HREF}">{TEL}</a>, e-mail <a href="mailto:{MAIL}">{MAIL}</a>. Represented by Stephan Bökelmann.</p>
<h2>2. Hosting (GitHub Pages)</h2>
<p>This website is hosted on GitHub Pages, a service of GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. When you access the site, GitHub processes technically necessary data (IP address, time, page requested, user agent) in server log files to deliver the site and ensure security. The legal basis is our legitimate interest in a secure and efficient operation of the website (Art. 6 (1) (f) GDPR). GitHub is certified under the EU-US Data Privacy Framework. More: <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<h2>3. Contacting us</h2>
<p>If you contact us by e-mail or phone, we process your details to handle the enquiry and follow-up questions (Art. 6 (1) (b) GDPR for pre-contractual measures, otherwise (f)). Data is deleted once it is no longer needed for that purpose and no statutory retention obligations apply.</p>
<h2>4. External links</h2>
<p>This site links to external sites (e.g. maxclerkwell.tech, skainet.io, LinkedIn, GitHub, OpenStreetMap). Once you click, the privacy policy of the respective provider applies.</p>
<h2>5. Your rights</h2>
<p>You have the right of access (Art. 15 GDPR), rectification (Art. 16), erasure (Art. 17), restriction of processing (Art. 18), data portability (Art. 20) and objection (Art. 21). You may lodge a complaint with a supervisory authority; ours is the Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen.</p>
<p>Last updated: {TODAY}. The German version is legally binding.</p>
""","zh":f"""
<p>本网站不使用 Cookie，不进行跟踪，不嵌入任何第三方服务。字体与图片均由本域名提供。</p>
<h2>1. 数据控制者</h2>
<p>nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)，Herner Str. 299, Gebäude B29, 44809 Bochum，德国。电话 <a href="{TEL_HREF}">{TEL}</a>，电子邮件 <a href="mailto:{MAIL}">{MAIL}</a>。法定代表：Stephan Bökelmann。</p>
<h2>2. 托管（GitHub Pages）</h2>
<p>本网站托管于 GitHub, Inc.（88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA）的 GitHub Pages 服务。访问网站时，GitHub 会在服务器日志中处理技术上必要的数据（IP 地址、时间、访问页面、User-Agent），以提供网页并保障安全。法律依据为我们对网站安全高效运行的合法利益（GDPR 第 6 条第 1 款 f 项）。详情：<a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub 隐私声明</a>。</p>
<h2>3. 联系我们</h2>
<p>当您通过电子邮件或电话联系我们时，我们会为处理您的请求及后续问题而处理您的信息（GDPR 第 6 条第 1 款 b 项或 f 项）。数据在不再需要且无法定保存义务时删除。</p>
<h2>4. 外部链接</h2>
<p>本站链接至外部网站（如 maxclerkwell.tech、skainet.io、LinkedIn、GitHub、OpenStreetMap）。点击后适用相应提供方的隐私政策。</p>
<h2>5. 您的权利</h2>
<p>您享有访问权（GDPR 第 15 条）、更正权（第 16 条）、删除权（第 17 条）、限制处理权（第 18 条）、数据可携权（第 20 条）和反对权（第 21 条）。您可向监管机构投诉；我们的主管机构为北莱茵-威斯特法伦州数据保护与信息自由专员。</p>
<p>更新日期：{TODAY}。以德文版本为准。</p>
"""}[L],
    )
    return C

# ---------------------------------------------------------------- JSON-LD
def org_node():
    return {
      "@type": ["Organization","ProfessionalService"],
      "@id": ORG_ID,
      "name": "nabla B",
      "alternateName": ["∇B","nabla-B","nabla B engineering"],
      "legalName": "nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)",
      "url": BASE + "/",
      "logo": {"@type":"ImageObject","url": BASE + "/assets/img/og-image.png","width":1200,"height":630},
      "image": BASE + "/assets/img/og-image.png",
      "description": "Engineering office in Bochum, Germany: design and development of embedded devices — architecture, PCB design, certification, software bring-up for MCU, FPGA and Zynq, firmware. Decentralised measurement & data acquisition, consulting and training. Part of the AI-Gruppe.",
      "foundingDate": "2020-07-20",
      "founder": {"@id": PERSON_STEPHAN},
      "employee": [{"@id":PERSON_STEPHAN},{"@id":PERSON_TABEA},{"@id":PERSON_MEIHUI},{"@id":PERSON_VANESSA},{"@id":PERSON_ATIYEH}],
      "numberOfEmployees": {"@type":"QuantitativeValue","value":4},
      "telephone": "+49-234-58545811",
      "email": "mailto:" + MAIL,
      "address": {"@type":"PostalAddress","streetAddress":"Herner Str. 299, Gebäude B29","addressLocality":"Bochum","postalCode":"44809","addressRegion":"NRW","addressCountry":"DE"},
      "areaServed": ["DE","EU","CN"],
      "openingHoursSpecification": [{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"13:30"}],
      "contactPoint": [{"@type":"ContactPoint","contactType":"customer service","name":"Vanessa Wilcken","telephone":"+49-234-58545811","email":"mailto:" + MAIL,"availableLanguage":["de","en","zh"],"hoursAvailable":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"13:30"}}],
      "identifier": [{"@type":"PropertyValue","propertyID":"German Trade Register","value":"Amtsgericht Bochum HRB 18817"}],
      "vatID": "DE338747475",
      "taxID": "DE338747475",
      "brand": {"@id": AIGRUPPE_ID},
      "memberOf": [{"@type":"Organization","name":"IHK Mittleres Ruhrgebiet","url":"https://www.bochum.ihk.de/"}],
      "knowsAbout": ["embedded systems","PCB design","KiCad","FPGA","Zynq","Yocto Linux","microcontroller firmware","EMC certification","data acquisition","decentralised measurement","condition monitoring","observability"],
      "sameAs": ["https://github.com/nabla-B","https://maxclerkwell.tech/imprint/","https://maxclerkwell.tech/about/","https://gruppe.ai/"],
      "priceRange": "Tagessatz ab 80 € netto",
      "makesOffer": [
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Embedded hardware development","serviceType":"PCB design, certification, bring-up"}},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Embedded firmware for MCU, FPGA and Zynq"}},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Decentralised measurement and data acquisition"}},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Consulting and training in digital measurement technology"}},
      ],
    }

def person_nodes(lang):
    T = content(lang)["team"]["people"]
    out=[]
    for p in T:
        n={"@type":"Person","@id":p["pid"],"name":p["name"],"givenName":p["name"].split()[0],"familyName":p["name"].split()[-1],
           "jobTitle":p["jobTitle"],"worksFor":{"@id":ORG_ID},"url": url(lang,"team")+"#"+p["id"],"description":p["bio"]}
        if p["img"]: n["image"]=BASE+p["img"]
        if p["sameAs"]: n["sameAs"]=p["sameAs"]
        if p["alt"]: n["alternateName"]=p["alt"]
        if p["knows"]: n["knowsAbout"]=p["knows"]
        def cat(e):
            e2=e.lower()
            return "doctoral degree" if ("promotion" in e2 or "phd" in e2 or "博士" in e) else "master degree" if (e2.startswith("m.") or e2.startswith("mba") or "硕士" in e or "mba" in e2) else "bachelor degree"
        if p["edu"]: n["hasCredential"]=[{"@type":"EducationalOccupationalCredential","credentialCategory":cat(e),"name":e} for e in p["edu"]]
        if p["alumni"]: n["alumniOf"]=[{"@type":"CollegeOrUniversity","name":a,"url":u} for a,u in p["alumni"]]
        if p["id"]=="stephan-boekelmann":
            n.update({"url":"https://maxclerkwell.tech/","mainEntityOfPage":"https://maxclerkwell.tech/about/",
                      "identifier":{"@type":"PropertyValue","propertyID":"ORCID","value":"0000-0002-2119-0064"},
                      "disambiguatingDescription":"Engineer and physicist in Bochum, Germany (Auto-Intern GmbH / skAInet, nabla B, Ruhr-Universität Bochum), known online as MaxClerkwell. Not the actor Stefan Bockelmann, and not related to the UK agency ClerksWell.",
                      "worksFor":[{"@id":ORG_ID},{"@id":AUTOINTERN_ID}],
                      "affiliation":[{"@id":AUTOINTERN_ID},{"@type":"CollegeOrUniversity","name":"Ruhr-Universität Bochum","url":"https://www.ruhr-uni-bochum.de/","sameAs":"https://ror.org/04tsk2644"}],
                      "subjectOf":[{"@type":"WebPage","url":"https://maxclerkwell.tech/talks/","name":"Talks & Conference Appearances"},
                                   {"@type":"WebPage","url":"https://maxclerkwell.tech/publications/","name":"Publications, Patents & Software"},
                                   {"@type":"WebPage","url":"https://edge-compute.skainet.io/team","name":"skAInet Edge-Compute team"}],
                      "knowsAbout":[*p["knows"], {"@id":EDGE_PRODUCT_ID}]})
        if p["id"]=="tabea-boekelmann": n.update({"affiliation":{"@id":AUTOINTERN_ID},"mainEntityOfPage":url(lang,"team")+"#"+p["id"]})
        if p["id"]=="meihui-huang": n.update({"affiliation":[{"@type":"CollegeOrUniversity","name":"Ruhr-Universität Bochum","department":"Institut für Experimentalphysik I – AG Hadronen und Kerne","url":"https://www.ep1.ruhr-uni-bochum.de/"},{"@type":"WebSite","@id":"https://maxclerkwell.tech/#website","name":"MaxClerkwell"}],"homeLocation":{"@type":"Place","name":"Witten, Germany"},"nationality":{"@type":"Country","name":"China"},"mainEntityOfPage":url(lang,"team")+"#"+p["id"]})
        if p["id"]=="vanessa-wilcken": n.update({"email":MAIL,"telephone":"+49-234-58545811","mainEntityOfPage":url(lang,"team")+"#"+p["id"]})
        if p["id"]=="atiyeh-chatrsefid": n.update({"email":MAIL_ATIYEH,"mainEntityOfPage":url(lang,"team")+"#"+p["id"]})
        out.append(n)
    return out

def jsonld(lang, page, C):
    P=C[page]
    website={"@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":"nabla B","publisher":{"@id":ORG_ID},"inLanguage":["de","en","zh-Hans"]}
    types={"index":"WebPage","leistungen":"CollectionPage","referenzen":"CollectionPage","team":"AboutPage","kontakt":"ContactPage","impressum":"WebPage","datenschutz":"WebPage"}
    webpage={"@type":types[page],"@id":url(lang,page)+"#webpage","url":url(lang,page),"name":P["title"],"description":P["desc"],"inLanguage":HTMLLANG[lang],"isPartOf":{"@id":BASE+"/#website"},"about":{"@id":ORG_ID},"dateModified":TODAY}
    graph=[org_node(),website,webpage]
    # cross-site entities referenced (thin stubs with canonical @ids)
    graph.append({"@type":"Brand","@id":AIGRUPPE_ID,"name":"AI-Gruppe","url":"https://gruppe.ai/",
                  "description":"Dachmarke (keine juristische Person) für Auto-Intern GmbH, CCD Car Diagnostics, nabla B, nerd_force1, open Skunkforce e.V. und das skAInet-Projekt."})
    graph.append({"@type":"Organization","@id":AUTOINTERN_ID,"name":"Auto-Intern GmbH","url":"https://www.auto-intern.de","email":"mailto:info@auto-intern.de",
                  "brand":[{"@id":"https://www.skainet.io/#brand"},{"@id":AIGRUPPE_ID}],
                  "sameAs":["https://www.skainet.io","https://edge-compute.skainet.io/","https://github.com/auto-intern-skainet"]})
    if page in ("index","team"): graph += person_nodes(lang)
    if page in ("index","referenzen"):
        items=[]
        for i,r in enumerate(REFS):
            name,desc=r[lang]
            node={"@type":"CreativeWork","name":name,"description":desc,"contributor":{"@id":ORG_ID},"temporalCoverage":r["years"]}
            if r["key"]=="edge": node={"@type":"Product","@id":EDGE_PRODUCT_ID,"name":"skAInet Edge-Compute","url":"https://edge-compute.skainet.io/","manufacturer":{"@id":AUTOINTERN_ID},"contributor":{"@id":PERSON_STEPHAN}}
            if r["links"]: node["url"]=node.get("url",r["links"][0][1])
            items.append({"@type":"ListItem","position":i+1,"item":node})
        graph.append({"@type":"ItemList","@id":url(lang,"referenzen")+"#projects","name":C["referenzen"]["h1"],"itemListElement":items})
    if page!="index":
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"nabla B","item":url(lang,"index")},{"@type":"ListItem","position":2,"name":P["h1"],"item":url(lang,page)}]})
    return json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False,indent=1)

# ---------------------------------------------------------------- templates
def esc(s): return html.escape(s, quote=True)

REF_SCRIPT = """<script>
(function(){
  try {
    var p=new URLSearchParams(location.search), d=document.getElementById('ref-modal');
    if(p.get('ref')!=='maxclerkwell.tech'||!d||!d.showModal||sessionStorage.getItem('ref-mc'))return;
    sessionStorage.setItem('ref-mc','1');
    d.showModal();
    d.addEventListener('click',function(e){if(e.target===d)d.close();});
    p.delete('ref'); var q=p.toString();
    history.replaceState(null,'',location.pathname+(q?'?'+q:'')+location.hash);
  } catch(e) {}
})();
</script>"""

def layout(lang, page, C, body):
    P=C[page]; U=UI[lang]
    alts="".join(f'<link rel="alternate" hreflang="{HTMLLANG[l]}" href="{url(l,page)}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url("de",page)}">'
    CUR=' aria-current="page"'; CURT=' aria-current="true"'
    nav="".join(f'<a href="{path(lang,p)}"{CUR if p==page else ""}>{t}</a>' for p,t in U["nav"])
    langsw="".join(f'<a href="{path(l,page)}" hreflang="{HTMLLANG[l]}" lang="{HTMLLANG[l]}" title="{LANGNAME[l][2]}"{CURT if l==lang else ""}><span class="f">{LANGNAME[l][0]}</span>{LANGNAME[l][1]}</a>' for l in LANGS)
    legal="".join(f'<li><a href="{path(lang,p)}">{t}</a></li>' for p,t in U["legal"])
    year=datetime.date.today().year
    modal=f'<dialog id="ref-modal" class="ref-modal" aria-labelledby="ref-modal-title"><form method="dialog"><h2 id="ref-modal-title">{U["ref_title"]}</h2><p>{U["ref_text"]}</p><p class="ref-modal-actions"><a href="https://maxclerkwell.tech/">{U["ref_back"]}</a><button value="ok" autofocus>{U["ref_ok"]}</button></p></form></dialog>'+REF_SCRIPT
    return f"""<!DOCTYPE html>
<html lang="{HTMLLANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(P["title"])}</title>
<meta name="description" content="{esc(P["desc"])}">
<link rel="canonical" href="{url(lang,page)}">
{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="nabla B"><meta property="og:title" content="{esc(P["title"])}"><meta property="og:description" content="{esc(P["desc"])}"><meta property="og:url" content="{url(lang,page)}"><meta property="og:image" content="{BASE}/assets/img/og-image.png"><meta property="og:locale" content="{ {"de":"de_DE","en":"en_GB","zh":"zh_CN"}[lang] }">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#323942">
<link rel="icon" href="/assets/img/logo-mark.svg" type="image/svg+xml"><link rel="icon" href="/assets/img/favicon-64.png" sizes="64x64" type="image/png"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/cmunbmr.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/cmunbsr.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
<script type="application/ld+json">
{jsonld(lang,page,C)}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{path(lang,"index")}" aria-label="nabla B – {U["nav"][0][1]}"><img src="/assets/img/logo.svg" alt="nabla B Ingenieurbüro & Dienstleistung-UG (haftungsbeschränkt)" width="228" height="86"></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">{U["menu"]}</button>
<nav class="nav" id="nav">{nav}</nav>
<div class="lang" aria-label="Language">{langsw}</div>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="cols">
<div><img class="flogo" src="/assets/img/logo.svg" alt="nabla B" width="170" height="64"><p>Herner Str. 299, Gebäude B29<br>44809 Bochum, Germany</p><p>{U["footer_group"]}</p></div>
<div><h4>{U["footer_contact"]}</h4><ul><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{TEL_HREF}">{TEL}</a></li><li>{U["footer_office"]}</li><li>{U["footer_hours"]}</li></ul></div>
<div><h4>nabla B</h4><ul>{"".join(f'<li><a href="{path(lang,p)}">{t}</a></li>' for p,t in U["nav"][1:])}{legal}</ul></div>
<div><h4>Links</h4><ul><li>{U["footer_blog"]}</li><li><a href="https://edge-compute.skainet.io/">skAInet Edge-Compute</a></li><li><a href="https://github.com/nabla-B">GitHub</a></li><li><a href="/assets/nablaB-corporate-design.pdf">{U["cd"]}</a></li></ul></div>
</div>
<div class="legal"><span>{U["copyright"].format(y=year)}</span><span>Amtsgericht Bochum HRB 18817 · USt-ID DE338747475</span></div>
</div></footer>
{modal}
</body>
</html>
"""

def ref_card(lang, r):
    name,desc=r[lang]
    links="".join(f'<a href="{u}" rel="noopener">{esc(t)} →</a>' for t,u in r["links"])
    return f'<article class="ref"><h3>{esc(name)}</h3><div class="meta">{esc(r["years"])} · {esc(r["client"])}</div><p>{esc(desc)}</p><div class="links">{links}</div></article>'

def cta_link(subject): return f"mailto:{MAIL}?subject={subject.replace(' ','%20')}"

def page_index(lang,C):
    P=C["index"]
    pillars="".join(f"<li>{esc(x)}</li>" for x in P["pillars"])
    cards="".join(f'<div class="card"><h3>{esc(h)}</h3><p>{esc(t)}</p></div>' for h,t in P["cards"])
    refs="".join(ref_card(lang,r) for r in REFS[:6])
    return f"""
<section class="hero"><div class="wrap"><div class="hero-inner">
<h1>{P["hero_h1"]}</h1>
<p class="lead">{esc(P["hero_lead"])}</p>
<ul class="pillars">{pillars}</ul>
<div class="cta-row"><a class="btn" href="{cta_link(P["cta_mail_subject"])}">{esc(P["cta"])}</a><a class="btn ghost" href="{TEL_HREF}">{TEL}</a><p class="cta-note">{esc(P["cta_note"])}</p></div>
</div></div></section>
<section><div class="wrap"><div class="sec-title"><h2>{esc(P["what_h"])}</h2></div><p class="sec-intro">{esc(P["what_intro"])}</p><div class="grid">{cards}</div><p style="margin-top:22px"><a href="{path(lang,"leistungen")}">{UI[lang]["nav"][1][1]} →</a></p></div></section>
<section class="alt"><div class="wrap"><div class="sec-title"><h2>{esc(P["refs_h"])}</h2></div><p class="sec-intro">{esc(P["refs_intro"])}</p><div class="refs">{refs}</div><p style="margin-top:22px"><a class="btn dark" href="{path(lang,"referenzen")}">{esc(P["refs_more"])}</a></p></div></section>
<section><div class="wrap"><div class="sec-title"><h2>{esc(P["blog_h"])}</h2></div><p class="sec-intro">{P["blog_p"]}</p></div></section>
<section class="alt"><div class="wrap"><div class="sec-title"><h2>{esc(P["contact_h"])}</h2></div>
<div class="contact-box"><div class="card"><h3>{C["kontakt"]["mail_h"]}</h3><p class="big"><a href="mailto:{MAIL}">{MAIL}</a></p><p>{C["kontakt"]["intro"]}</p></div><div class="card"><h3>{C["kontakt"]["tel_h"]}</h3><p class="big"><a href="{TEL_HREF}">{TEL}</a></p><p>{C["kontakt"]["hours"]}</p></div></div>
</div></section>
"""

def page_leistungen(lang,C):
    P=C["leistungen"]
    blocks="".join(f'<div class="card"><h3>{esc(h)}</h3><ul class="tri">{"".join(f"<li>{esc(i)}</li>" for i in items)}</ul></div>' for h,items in P["blocks"])
    return f"""
<section><div class="wrap"><div class="sec-title"><h1>{esc(P["h1"])}</h1></div><p class="sec-intro">{esc(P["intro"])}</p><div class="grid grid-3" style="margin-top:28px">{blocks}</div></div></section>
<section class="alt"><div class="wrap"><div class="sec-title"><h2>{esc(P["pricing_h"])}</h2></div><p class="sec-intro">{esc(P["pricing"])}</p><p><a class="btn dark" href="{cta_link(C["index"]["cta_mail_subject"])}">{esc(P["cta"])}</a></p></div></section>
"""

def page_referenzen(lang,C):
    P=C["referenzen"]
    return f"""
<section><div class="wrap"><div class="sec-title"><h1>{esc(P["h1"])}</h1></div><p class="sec-intro">{esc(P["intro"])}</p><div class="refs" style="margin-top:28px">{"".join(ref_card(lang,r) for r in REFS)}</div></div></section>
"""

def page_team(lang,C):
    P=C["team"]
    cards=""
    for p in P["people"]:
        pic=f'<img class="pic" src="{p["img"]}" alt="{esc(p["name"])}" width="140" height="140" loading="lazy">' if p["img"] else f'<div class="initials" aria-hidden="true">{"".join(w[0] for w in p["name"].split()[:2])}</div>'
        links="".join(f'<a href="{u}" rel="noopener">{esc(t)}</a>' for t,u in p["links"])
        edu=f'<ul class="edu">{"".join(f"<li>{esc(e)}</li>" for e in p["edu_short"])}</ul>' if p["edu_short"] else ""
        cards+=f'<article class="person" id="{p["id"]}">{pic}<div class="ptext"><h3>{esc(p["name"])}</h3><div class="role">{esc(p["role"])}</div><p>{esc(p["short"])}</p>{edu}<div class="links">{links}</div></div></article>'
    return f"""
<section><div class="wrap"><div class="sec-title"><h1>{esc(P["h1"])}</h1></div><p class="sec-intro">{esc(P["intro"])}</p><div class="team" style="margin-top:28px">{cards}</div><p class="disambig">{esc(P["disambig"])}</p></div></section>
"""

def page_kontakt(lang,C):
    P=C["kontakt"]
    return f"""
<section><div class="wrap"><div class="sec-title"><h1>{esc(P["h1"])}</h1></div><p class="sec-intro">{P["intro"]}</p>
<div class="contact-box two" style="margin-top:28px">
<div class="card"><h3>{P["mail_h"]}</h3><p class="big"><a href="mailto:{MAIL}">{MAIL}</a></p><p><a class="btn dark" href="{cta_link(P["cta_mail_subject"])}">{esc(P["cta"])}</a></p></div>
<div class="card"><h3>{P["tel_h"]}</h3><p class="big"><a href="{TEL_HREF}">{TEL}</a></p><p><strong>{P["hours_h"]}:</strong> {P["hours"].replace("<br>", ", ")}</p></div>
<div class="card"><h3>{P["addr_h"]}</h3><p>{P["addr"]}</p></div>
<div class="card"><h3>{P["map_h"]}</h3><p>{esc(P["map_p"])}</p><p><a href="{P["map_link"]}" rel="noopener">OpenStreetMap →</a></p></div>
</div></div></section>
"""

def page_prose(lang,C,page):
    P=C[page]
    return f"""<section><div class="wrap prose"><div class="sec-title"><h1>{esc(P["h1"])}</h1></div>{P["body"]}</div></section>"""

RENDER={"index":page_index,"leistungen":page_leistungen,"referenzen":page_referenzen,"team":page_team,"kontakt":page_kontakt,
        "impressum":lambda l,C:page_prose(l,C,"impressum"),"datenschutz":lambda l,C:page_prose(l,C,"datenschutz")}

# ---------------------------------------------------------------- aux files
def llms_txt():
    refs="\n".join(f"- {r['en'][0]} ({r['years']}, {r['client']}): {r['en'][1]}" + (" Links: "+", ".join(f"[{t}]({u})" for t,u in r['links']) if r['links'] else "") for r in REFS)
    return f"""# nabla B

> nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt) is an engineering office in Bochum, Germany, founded 2020-07-20 by Stephan Bökelmann. It designs and develops embedded devices — from architecture via PCB design and certification to software bring-up for MCU, FPGA and Zynq, all the way to firmware — and builds decentralised measurement and data-acquisition (DAQ) systems for mid-sized industry. It also offers consulting and training in digital measurement technology. nabla B is part of the AI-Gruppe umbrella brand (https://gruppe.ai/) together with Auto-Intern GmbH / skAInet.

Canonical entity IDs (JSON-LD): organisation `{ORG_ID}`; founder/managing director `{PERSON_STEPHAN}` (Stephan Bökelmann, ORCID 0000-0002-2119-0064, personal site https://maxclerkwell.tech/). The same organisation is described on https://maxclerkwell.tech/imprint/ and https://maxclerkwell.tech/about/; the skAInet Edge-Compute product nabla B architected is `{EDGE_PRODUCT_ID}` (https://edge-compute.skainet.io/, manufacturer Auto-Intern GmbH).

Languages: German (default, {BASE}/), English ({BASE}/en/), Simplified Chinese ({BASE}/zh/).

## Contact
- Contact person: Vanessa Wilcken (executive assistant / office)
- E-mail: {MAIL}
- Phone: {TEL}
- Office hours: Monday–Friday 09:00–13:30 CET
- Address: Herner Str. 299, Gebäude B29, 44809 Bochum, Germany
- Commercial register: Amtsgericht Bochum HRB 18817 · VAT ID DE338747475
- Managing director: Stephan Bökelmann
- Day rate from € 80 net; initial consultation free. Call to action: book an appointment with Stephan Bökelmann via office@nabla-b.engineering.

## Services
- Architecture & system design for embedded devices
- PCB design (KiCad), design for manufacturing, supply chain incl. China
- EMC / CE certification preparation and support (Germany and China)
- Software bring-up for microcontrollers, FPGAs (VHDL/Verilog) and Zynq SoCs (U-Boot, device tree, Yocto Linux with SBOM)
- Firmware: drivers, protocols, OTA updates, telemetry
- Decentralised measurement & DAQ, monitoring/observability infrastructure
- Consulting (architecture reviews, toolchain rescue) and training for engineers

## Team
- Stephan Bökelmann (alias MaxClerkwell, 施泓杰) — Managing Director, engineer & physicist; B.Eng., M.Eng. (THGA Bochum), PhD candidate RUB. ID {PERSON_STEPHAN}. Profiles: https://maxclerkwell.tech/, https://www.linkedin.com/in/accelerator-stephan/, https://orcid.org/0000-0002-2119-0064, https://x.com/maxclerkwell, https://instagram.com/_maxclerkwell, https://www.researchgate.net/profile/Stephan-Boekelmann
- Tabea Bökelmann (also Tabea Viktoria Bökelmann / Boekelmann / Röthemeyer) — Senior Frontend Consultant, Angular & JavaScript; B.Sc. Physics (particle physics, DAQ), B.Sc. and M.Sc. Applied Computer Science (RISC-V, compilers, "Git with Features"), all Ruhr-Universität Bochum. ID {PERSON_TABEA}. Profiles: https://www.linkedin.com/in/tabea-b%C3%B6kelmann-0b9794198/, https://www.researchgate.net/profile/Tabea-Roethemeyer
- Meihui Huang (黄美慧, Huang Mei Hui) — Physicist, working student for research and outreach; B.Sc. Physics Nankai University Tianjin (decay-chain analysis with ROOT), M.Sc. student RUB EP1 Hadrons and Nuclei group; social media executive for maxclerkwell.tech. ID {PERSON_MEIHUI}. Profiles: https://www.linkedin.com/in/meihui-huang/, https://www.researchgate.net/profile/Meihui-Huang
- Vanessa Wilcken — Executive assistant, first point of contact (office@nabla-b.engineering, +49 234 58545811). ID {PERSON_VANESSA}. Profile: https://www.linkedin.com/in/vanessa-wilcken-1436b320a/
- Atiyeh Chatrsefid — Business development (customer acquisition, partnerships, proposals); MBA Artificial Intelligence (Brand University of Applied Sciences), Computer Science (Ruhr-Universität Bochum); previously commercial lead at Wisdom Bridge AI, AI strategy consultant, Deloitte project management intern. Contact: {MAIL_ATIYEH}. ID {PERSON_ATIYEH}. Profile: https://www.linkedin.com/in/atiyeh-chatrsefid-/

## References (selection; many customer projects are under NDA)
{refs}

## Pages
- [Home (DE)]({BASE}/) · [EN]({BASE}/en/) · [ZH]({BASE}/zh/)
- [Services]({BASE}/leistungen/) · [EN]({BASE}/en/services/) · [ZH]({BASE}/zh/services/)
- [References]({BASE}/referenzen/) · [EN]({BASE}/en/references/) · [ZH]({BASE}/zh/references/)
- [Team]({BASE}/team/) · [EN]({BASE}/en/team/) · [ZH]({BASE}/zh/team/)
- [Contact]({BASE}/kontakt/) · [EN]({BASE}/en/contact/) · [ZH]({BASE}/zh/contact/)
- [Imprint]({BASE}/impressum/) · [Privacy]({BASE}/datenschutz/)

## Related sites
- https://maxclerkwell.tech/ — Stephan Bökelmann's technical blog (hobby and research projects; customer work mostly under NDA)
- https://edge-compute.skainet.io/ — skAInet Edge-Compute product page (Auto-Intern GmbH)
- https://skainet.io/ — skAInet brand
- https://gruppe.ai/ — AI-Gruppe umbrella brand
- https://github.com/nabla-B — GitHub organisation
"""

def sitemap():
    urls=""
    for p in PAGES:
        for l in LANGS:
            alts="".join(f'<xhtml:link rel="alternate" hreflang="{HTMLLANG[a]}" href="{url(a,p)}"/>' for a in LANGS)
            urls+=f'<url><loc>{url(l,p)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>\n'
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n'

def page404():
    return """<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404 – nabla B</title><link rel="stylesheet" href="/assets/css/site.css"><link rel="icon" href="/assets/img/logo-mark.svg"></head>
<body><main id="main"><section><div class="wrap prose"><a href="/"><img src="/assets/img/logo.svg" alt="nabla B" width="228" height="86"></a><h1>404</h1><p>Diese Seite gibt es nicht. / This page does not exist. / 页面不存在。</p><p><a href="/">nabla-b.engineering</a> · <a href="/en/">English</a> · <a href="/zh/">中文</a></p></div></section></main></body></html>
"""

def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p,"w",encoding="utf-8") as f: f.write(s)

def main():
    root=os.path.dirname(os.path.abspath(__file__))
    for lang in LANGS:
        C=content(lang)
        for page in PAGES:
            body=RENDER[page](lang,C)
            out=os.path.join(root, LANGS[lang], SLUGS[lang][page], "index.html")
            write(out, layout(lang,page,C,body))
    write(os.path.join(root,"llms.txt"), llms_txt())
    write(os.path.join(root,"sitemap.xml"), sitemap())
    write(os.path.join(root,"robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    write(os.path.join(root,"404.html"), page404())
    write(os.path.join(root,".nojekyll"), "")
    print("built", len(LANGS)*len(PAGES), "pages")

if __name__=="__main__": main()
