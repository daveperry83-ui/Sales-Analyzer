# Egipto · Oleorresinas: huecos difíciles

Fecha de consulta: 19 de noviembre de 2026. Complementa `index.html` y no lo reemplaza.

## Cómo leer este documento (importante)

En esta sesión casi ninguna página web se pudo abrir:

- **WebFetch** no resolvió ningún host que probé: trade.gov, customs.gov.eg, nfsa.gov.eg, wits.worldbank.org, indianspices.com, comtradeapi.un.org, zauba.com, camtomx.com y wikipedia.org.
- **Firecrawl** abrió dos páginas (Zauba y Camtom) y ejecutó consultas a UN Comtrade. Después **se quedó sin créditos**, a mitad de la tarea.
- **Bash/curl** hacia la API de Comtrade fue denegado por permisos.

Por eso cada dato lleva una etiqueta de evidencia:

| Etiqueta | Significado |
|---|---|
| **[A] Abierto** | Página o API leída directamente en esta sesión. Es fuente. |
| **[B] Solo buscador** | Aparece en el resumen de un buscador. **La página no se abrió.** Por la regla del encargo no es fuente: es una pista que hay que verificar. |

No se inventaron cifras. Si algo no está, se dice.

---

## 1. Importadores de oleorresinas y extractos de especias en Egipto

### Lo que se verificó

**[A] Registros de exportación india a Egipto, 2013–2016 (Zauba).** La página se abrió.
https://www.zauba.com/export-3pd/hs-code-3301/fp-egypt-hs-code.html

- Muestra 533 embarques de un solo exportador indio, con el nombre enmascarado («3pd»), hacia Egipto. Todos salen por Cochín, Delhi, Bangalore, Hyderabad o Nhava Sheva, entre feb 2013 y sep 2016. Suman US$8.169.395.
- La página **no muestra el nombre del importador egipcio**. Dice que hay «13 importadores», pero atribuye el dato a «US Customs Department», lo que no encaja con registros de aduana india. Fuente incoherente para nombres.
- Lo útil es la mezcla de productos que compra Egipto, por código nacional indio de 8 dígitos (número de embarques):

| Código | Producto | Embarques |
|---|---|---|
| 33019029 | Otras oleorresinas de especias | 156 |
| 33019022 | Capsicum | 64 |
| 33019013 | Pimienta | 42 |
| 33019023 | Cilantro | 30 |
| 33019014 | Cúrcuma | 29 |
| 33019021 | Clavo | 23 |
| 33019012 | Jengibre | 18 |
| 33019015 | Cardamomo | 17 |
| 33019017 | Nuez moscada | 16 |
| 33019016 | Apio | 11 |
| 33019024 | Comino | 10 |
| 33019011 | Fenogreco | 9 |
| 33019025 | Hinojo | 3 |

Los lotes son pequeños (15–540 kg). Ese perfil corresponde a una casa de sabores o a un formulador que compra una gama amplia, no a un procesador de volumen. **Es un dato histórico (2013–2016)** y no identifica al comprador.

### Pistas sin verificar (no son fuente)

| Empresa | Tipo probable | Qué compraría / origen | Evidencia | Estado |
|---|---|---|---|---|
| **Givaudan Egypt SAE** | Casa de sabores | Oleorresina de paprika desde China, 2019–2022 | [B] Resumen de buscador sobre Volza, «Paprika buyers in Egypt»: https://www.volza.com/p/paprika/buyers/buyers-in-egypt/ (el buscador dice que la página tiene unos 825 días) | No verificado. Volza no se pudo abrir con Firecrawl |
| **Symrise SAE** | Casa de sabores | Paprika (el resumen no aclara si es oleorresina o polvo), 2 embarques | [B] Misma página de Volza | No verificado |
| **Namaa Flavors & Fragrances (NFF)** | Casa de sabores local, fundada en 2015, planta en 10th of Ramadan | Compuestos de sabor y fragancia. Plan de unidad de aislamiento de aromas naturales por EGP 250 M (comunicado del 28 oct 2025). No hay evidencia de que compre oleorresinas | [B] https://www.zawya.com/en/press-release/companies-news/namaa-flavors-and-fragrances-invests-egp-250mln-to-launch-egypts-first-natural-aroma-isolation-unit-anlgul9k · https://www.arabfinance.com/en/news/newdetails/namaa-positions-egypt-as-an-aroma-ingredients-hub | Comprador plausible, sin registro aduanero |
| **Aromatic Flavours & Fragrances SAE (AFF)**, ex International Aromatics | Casa de sabores independiente, Alejandría, desde 1969 | Sabores en polvo, líquido, encapsulado y emulsión. No se confirma que compre oleorresinas | [B] Expositor en Fi Africa: https://visitor.figlobal.com/event/fi-africa-and-propak-mena-5/exhibitor/RXhoaWJpdG9yXzI0NDg5MzA= · Gulfood Manufacturing: https://gulfoodmanufacturing.com/exhibitors/aromatic-flavours-and-fragrances-sae | Comprador plausible |
| **Flavour House** (Giza, 6th of October) | Fabricante de sabores líquidos y en polvo | Sin datos de compra | [B] Directorio: https://yellowpages.com.eg/en/category/flavors,-fragrances,-coloring-extracts-and-essential-oils | Solo directorio |
| **Export Development Bank** (aparece como «mayor comprador» de paprika en Volza) | Banco: probable financiador de carta de crédito, no usuario final | n.d. | [B] Volza (misma URL) | Artefacto del registro, no es cliente |

**Conclusión del punto 1:** no se obtuvo ningún registro aduanero que se pudiera abrir y que nombre a un importador egipcio de oleorresinas. Volza, Eximpedia, Tridge y Trademo esconden los nombres tras un muro de pago o no se pudieron abrir. Las ferias (Fi Africa, Gulfood) y la prensa dan casas de sabores **locales** (NFF, AFF) que son compradores plausibles. Las multinacionales (Givaudan, Symrise) aparecen en Volza solo en el resumen del buscador. Tampoco se pudo consultar el directorio de la Cámara de Industrias Alimentarias (CFI).

---

## 2. Arancel y requisitos sanitarios para HS 3301.90 y colorantes naturales

### Arancel

- **No verificado.** No se pudo abrir el arancel oficial de la Autoridad Aduanera egipcia (customs.gov.eg), ni WITS/TRAINS, ni el Country Commercial Guide de trade.gov.
- [B] Los agregadores egipcios gomruky.com y egyptariffs.com tienen fichas por línea nacional de 10 dígitos, por ejemplo https://www.gomruky.com/tariff/3301290010. El resumen del buscador menciona un **14%** que parece ser el **IVA** (Egipto aplica 14% de IVA a la importación), no el arancel. También menciona un posible trámite de **aprobación previa de la Autoridad Egipcia del Medicamento (EDA) y de la NFSA** para liberar la mercancía. No verificado.
- [B] El Examen de Política Comercial de la OMC de 2018 da un arancel NMF aplicado medio de 19,1% (2017) para todas las líneas. Es un promedio, no la tasa de 3301.90: https://www.wto.org/english/tratop_e/tpr_e/s367_e.pdf
- [A, pero no aplica a Egipto] Camtom muestra 10% NMF para aceites esenciales **desde Egipto hacia México**. No es el arancel egipcio: https://camtomx.com/aranceles/aceites-esenciales/egipto
- Las preferencias que podrían aplicar (Agadir, COMESA, AfCFTA, acuerdo UE-Egipto) dependen del origen. Para India y China, los orígenes principales, no hay acuerdo preferencial con Egipto, así que regiría la tasa NMF. Esto es razonamiento, no dato verificado.

**Siguiente paso:** buscar 3301.90 (y 3203.00 para colorantes de origen vegetal) en el buscador de la Autoridad Aduanera egipcia o en gomruky.com con la red habilitada, o pedirlo a un despachante egipcio.

### Requisitos sanitarios, registro, etiquetado y halal (todo [B]: los informes no se pudieron abrir)

- **NFSA, Decisión 4/2020:** fija la lista positiva de colorantes y aditivos y sus niveles. Acepta los saborizantes aprobados por Codex. El certificado de análisis debe indicar el nombre científico del colorante y su concentración. Recomiendan confirmar con la NFSA la aceptación de cada colorante. Fuente: informe FAIRS de USDA, El Cairo, 2025 (EG2025-0025): https://www.fas.usda.gov/data/gain-report/2025/12/FAIRS%20Country%20Report%20Annual_Cairo_Egypt_EG2025-0025.pdf. No se encontró mención específica de paprika ni de cúrcuma.
- **Enmienda 2026** a la instrucción IN 211/2023 sobre criterios de uso de aditivos. Solo aparece en un resumen secundario: https://www.flavorist.com/key-regulatory-and-legal-updates-for-africas-food-and-flavor-sector-released-or-due-for-compliance-from-june-27-july-13-2026/. Número y vigencia no confirmados.
- **Decisión NFSA 1/2025 sobre OGM,** publicada el 4 ene 2026 con seis meses de gracia. Alcanza a aditivos y preparados de aditivos con material genéticamente modificado. Fuente: USDA GAIN EG2026-0001 (en apps.fas.usda.gov, host que no resuelve).
- **Decreto 43/2016 (registro de fábricas en GOEIC):** según USDA aplica a una lista de productos envasados para venta minorista. Un ingrediente a granel como la oleorresina probablemente no entra, pero no está confirmado. Texto del decreto: https://www.goeic.gov.eg/upload/online/2016/03/documents/files/en/1484.pdf
- **Halal:** si el embarque declara halal, cada envío debe llevar certificado de **IS EG Halal**, que el gobierno trata como única autoridad (USDA FAIRS 2024–2025). No se encontró que sea obligatorio para un ingrediente no cárnico sin declaración halal. Los clientes industriales suelen pedirlo igual (dato no verificado).
- **Documentos generales:** certificado de origen, certificado de libre venta o de exportación, y halal cuando aplique (USDA FAIRS). Debe añadirse el ACID/Nafeza ya documentado en `index.html`.
- **Etiquetado:** no se encontró la norma específica (ES 1546 de etiquetado de alimentos envasados u otra) para ingredientes a granel. Pendiente.

---

## 3. Precios recientes de oleorresinas (USD/kg)

Ninguna cifra de esta sección se abrió en su página. Todas son [B] y van como orientación, con fecha y unidad cuando el resumen las daba.

| Oleorresina | Precio | Unidad / grado | Fecha | Tipo | Fuente [B] |
|---|---|---|---|---|---|
| Paprika | US$25–40/kg | ASTA 40.000 | Oct 2026 | Lista de exportador indio, FOB puerto indio | https://www.botanikabharat.com/paprika-oleoresins.php |
| Paprika | ≈US$35,6/kg promedio | Sin grado (exportaciones indias, 520 t, US$18,5 M) | Año fiscal 2024–25 | Valor unitario de exportación | Misma página |
| Paprika | Spot +10–15% interanual | Sin grado | Inicio 2026 | Comentario de reporte de mercado | https://www.researchandmarkets.com/reports/6235548/oleoresin-paprika-market-analysis-trends |
| Paprika | US$40,16/kg (importación EE.UU.); Japón 69,14; Canadá 43,24 | Sin grado | Oct 2025 | Valor unitario aduanero | https://www.tridge.com/market-overview/paprika-oleoresin |
| Capsicum | ≈US$35/kg promedio | Sin SHU | 12 meses a 30 abr 2026 | Valor unitario de embarques | https://pharmaoffer.com/api-excipient-supplier/transactions/capsicum-oleoresin |
| Capsicum | India y Vietnam US$18–22/kg; EE.UU. 44,21; México 46,13 | Sin SHU | Nov 2025 | Valor unitario aduanero | https://www.tridge.com/market-overview/capsicum-oleoresin |
| Pimienta negra (extracto) | US$77,30/kg (feb 2026) vs US$45,77/kg (sep 2025) | Sin % de piperina; volumen bajo (≈28 t/mes) | Feb 2026 | Valor unitario de exportación india | https://www.tridge.com/market-overview/black-pepper-extract |
| Pimienta negra | INR 2.000–5.400/kg (SCFE hasta 8.500) | Sin especificación | Listados sin fecha fiable | Lista doméstica | https://dir.indiamart.com/impcat/black-pepper-oleoresin.html |
| Cúrcuma | INR 1.200–3.500/kg (algunos 4.200–10.500) | % de curcumina variable | Listados sin fecha fiable | Lista doméstica | https://www.exportersindia.com/indian-suppliers/oleoresin.htm |
| Apio, comino, cilantro | **Sin precio 2026 encontrado** | — | — | — | Solo hay precios de semilla, por ejemplo apio entero FOB Nueva Delhi ≈€1,24/kg en marzo 2026: https://commodity-board.com/indian-celery-seed-fob-new-delhi-edges-higher-on-firm-export-interest |

**Referencia histórica [A]:** valores unitarios de exportación india a Egipto en la página de Zauba ya citada. Son lotes pequeños de 2015–2016, sin grado salvo capsicum:

- Capsicum 6,6%: US$21,84/kg
- Pimienta negra: US$44,53/kg
- Pimienta blanca: US$142,39/kg
- Cúrcuma: US$26,73/kg
- Jengibre: US$33,26/kg
- Clavo: US$71,77/kg
- Cardamomo: US$168,20/kg
- Casia: US$103,28/kg
- Apio: US$8,84/kg (dato anómalo, posiblemente un oleorresina diluida o soluble)

Tienen diez años. No se usan como precio actual.

No se encontraron precios publicados por el Spices Board India ni por USDA para oleorresinas en 2026. indianspices.com y apps.fas.usda.gov no resolvieron.

---

## 4. Productores egipcios de oleorresinas y aceites de semillas

No se encontró **ningún productor egipcio de oleorresina de paprika, capsicum, pimienta o cúrcuma** con evidencia más allá de directorios. Para aceites esenciales de semillas sí hay actores con algo más de respaldo (todo [B]):

| Empresa | Qué hace | Evidencia más fuerte encontrada | Capacidad / certificaciones |
|---|---|---|---|
| **A. Fakhry & Co.** (El Cairo, desde 1955) | Aceites esenciales, absolutos, concretos e hidrolatos; orgánico USDA/NOP y UE declarado | Expositor en World Perfumery Congress 2025: https://app.swapcard.com/event/perfumerycongress25/exhibitor/RXhoaWJpdG9yXzIwNjY1OTQ= · Ficha en Perfumer & Flavorist: https://www.perfumerflavorist.com/home/company/21161197/a-fakhry-co | Sin capacidad publicada. No se confirmó que produzca comino o cilantro |
| **Hashem Brothers for Essential Oils & Aromatic Products** (El Cairo, desde 1974) | Jazmín, geranio, neroli, albahaca | Participante del Pacto Mundial de la ONU: https://unglobalcompact.org/what-is-gc/participants/4768-Hashem-Brothers-for-Essential-Oils-and-Aromatic-Products · Certificado Fair for Life: https://www.fairforlife.org/en/partenaire/hashem-brothers-for-essential-oils-aromatic-products-2/ | No hay evidencia de aceites de semillas ni de FSSC 22000 |
| **Fridal Egypt** (6th of October) | Aceites de cilantro, comino e hinojo por destilación | Sitio propio: http://www.fridalegypt.com/en/essential-oils | Sin certificaciones visibles. El listado es antiguo |
| **Al Sheikh for Export** | Aceites de cilantro, comino e hinojo dulce destilados en Egipto | Sitio propio: https://alsheikhforexport.com/products/index.html · Knowde: https://www.knowde.com/stores/al-sheikh-for-export | Declara ISO 9001 e ISO 22000 (autodeclarado) |
| **Spice Kingdom** (ya en `index.html`) | Declara oleorresinas y extractos | Perfil Nutrada | Autodeclarado |
| **Export Key** (El Cairo) | Se presenta como exportador de aceites esenciales y oleorresinas a granel | Solo directorio | Sin datos |

**Evidencia indirecta de exportación de aceite de comino egipcio:** el distribuidor neerlandés Ultra International vende «Cumin Seed Oil (Egypt)»: https://ultranl.com/products/cumin-seed-oil-egypt/ [B]. Robertet también lista aceite de comino de origen Egipto: https://matieres-premieres.robertet.com/cumin-oil [B]. Lo mismo vale para el sourcing interno.

**Evidencia de que Egipto compra en vez de producir:** los registros de Zauba [A] muestran que Egipto importaba de India oleorresinas de **comino, cilantro, fenogreco, hinojo y apio** (sección 1). Eso apunta a que la extracción local de oleorresinas de semilla era limitada, al menos en 2013–2016.

No se encontraron datos de capacidad (toneladas al año) de ningún destilador egipcio de semillas.

---

## 5. Cantidad de oleorresinas en el comercio de Egipto

### Códigos nacionales

- **[A] UN Comtrade, datos por línea arancelaria nacional** (alexandria_library_read, provider `comtradeplus-un-org`, capacidad `trade-statistics/tariffline_data`, reportero 818). Egipto reporta **solo al nivel HS6 (330190)** para 2023, 2024 y 2025. **No publica subdivisiones nacionales** que separen oleorresinas, y **el peso neto y la cantidad vienen en 0 o vacíos**. No se puede calcular el volumen en kilos de oleorresina desde los datos egipcios. Fuente de la consulta: `https://comtradeapi.un.org/public/v1/previewTariffline/C/A/HS?reporterCode=818&period=2025&flowCode=M&cmdCode=330190`
- Que el arancel nacional egipcio tenga líneas de 10 dígitos dentro de 3301.90 (gomruky.com muestra líneas de 10 dígitos en 3301.29) **no está verificado**: no se pudo abrir.

### Dato nuevo: importaciones de 2025 [A]

Fuente: UN Comtrade, línea arancelaria, Egipto como reportero, HS 330190, importaciones (valor CIF en US$).

| Socio | 2023 | 2024 | 2025 | Peso 2025 |
|---|---|---|---|---|
| India | 2.003.868 | 3.357.613 | **5.133.651** | 81% |
| China | 2.028.444 | 1.683.597 | **625.166** | 10% |
| Indonesia | n.d. en el top | 202.538 | 270.786 | 4% |
| Líbano | 41.643 | 59.804 | 96.693 | 1,5% |
| Canadá | 37.581 | 36.993 | 61.001 | 1% |
| **Total (suma de socios)** | **4.283.801** | **5.629.372** | **6.332.584** | |

- 2025 sube **+12,5%** frente a 2024. India vuelve a dominar con 81% y China cae a 10%. El cambio de origen cada año que describe `index.html` se confirma.
- El total de 2024 coincide con el de `index.html` (US$5,6 M; India 60%, China 30%).
- Exportaciones 2024 [A]: US$6.745.446. Arabia Saudita 1,85 M, Libia 1,54 M, Francia 1,20 M, Yemen 0,47 M. Coincide con `index.html`.
- **Exportaciones 2025: no consultadas.** La consulta con socio «0» (mundo) devolvió vacío porque los datos por línea no traen agregado mundial. No quedaron créditos para repetirla por socio.

### Vía para separar oleorresinas: datos espejo

India sí separa oleorresinas a 8 dígitos: 33019011 fenogreco, …12 jengibre, …13 pimienta, …14 cúrcuma, …15 cardamomo, …16 apio, …17 nuez moscada, …21 clavo, …22 capsicum, …23 cilantro, …24 comino, …25 hinojo, …29 otras especias, …90 otros. Lo confirman los códigos de la página de Zauba [A].

Consultar `tariffline_data` con reportero 699 (India), socio 818 (Egipto), HS 330190 y flujo X para 2024–2025 daría el desglose por oleorresina de lo que India envía a Egipto, que es 60–81% del total. La consulta **no se pudo ejecutar** por falta de créditos de Firecrawl, y la API directa no resuelve desde esta sesión. Es la prioridad número 1 para la próxima sesión. Lo mismo vale con China (156) como reportero.

---

## Tabla de fuentes

| # | Fuente | URL | Evidencia | Consulta |
|---|---|---|---|---|
| 1 | Zauba, exportaciones indias a Egipto, HS 3301 (2013–2016) | https://www.zauba.com/export-3pd/hs-code-3301/fp-egypt-hs-code.html | A | 19 nov 2026 |
| 2 | UN Comtrade, línea arancelaria, Egipto (818), HS 330190, M 2023/2024/2025 y X 2024 | https://comtradeapi.un.org/public/v1/previewTariffline/C/A/HS?reporterCode=818&period=2025&flowCode=M&cmdCode=330190 (y period=2023, 2024; flowCode=X) | A (vía Alexandria) | 19 nov 2026 |
| 3 | Camtom, arancel de México a aceites esenciales egipcios (no aplica a Egipto) | https://camtomx.com/aranceles/aceites-esenciales/egipto | A | 19 nov 2026 |
| 4 | Volza, compradores de paprika en Egipto | https://www.volza.com/p/paprika/buyers/buyers-in-egypt/ | B | 19 nov 2026 |
| 5 | Zawya, comunicado de Namaa F&F (28 oct 2025) | https://www.zawya.com/en/press-release/companies-news/namaa-flavors-and-fragrances-invests-egp-250mln-to-launch-egypts-first-natural-aroma-isolation-unit-anlgul9k | B | 19 nov 2026 |
| 6 | Arab Finance, entrevista a Namaa | https://www.arabfinance.com/en/news/newdetails/namaa-positions-egypt-as-an-aroma-ingredients-hub | B | 19 nov 2026 |
| 7 | Fi Africa, expositor AFF | https://visitor.figlobal.com/event/fi-africa-and-propak-mena-5/exhibitor/RXhoaWJpdG9yXzI0NDg5MzA= | B | 19 nov 2026 |
| 8 | Gulfood Manufacturing, AFF | https://gulfoodmanufacturing.com/exhibitors/aromatic-flavours-and-fragrances-sae | B | 19 nov 2026 |
| 9 | Yellow Pages Egipto, sabores y extractos | https://yellowpages.com.eg/en/category/flavors,-fragrances,-coloring-extracts-and-essential-oils | B | 19 nov 2026 |
| 10 | Gomruky, arancel egipcio (línea 3301290010) | https://www.gomruky.com/tariff/3301290010 | B | 19 nov 2026 |
| 11 | OMC, Examen de Política Comercial de Egipto, 2018 | https://www.wto.org/english/tratop_e/tpr_e/s367_e.pdf | B | 19 nov 2026 |
| 12 | USDA FAIRS, El Cairo, 2025 | https://www.fas.usda.gov/data/gain-report/2025/12/FAIRS%20Country%20Report%20Annual_Cairo_Egypt_EG2025-0025.pdf | B | 19 nov 2026 |
| 13 | Flavorist, resumen regulatorio de África, jun–jul 2026 | https://www.flavorist.com/key-regulatory-and-legal-updates-for-africas-food-and-flavor-sector-released-or-due-for-compliance-from-june-27-july-13-2026/ | B | 19 nov 2026 |
| 14 | GOEIC, Decreto 43/2016 | https://www.goeic.gov.eg/upload/online/2016/03/documents/files/en/1484.pdf | B | 19 nov 2026 |
| 15 | Botanika Bharat, paprika (oct 2026) | https://www.botanikabharat.com/paprika-oleoresins.php | B | 19 nov 2026 |
| 16 | Research and Markets, oleorresina de paprika 2026–2031 | https://www.researchandmarkets.com/reports/6235548/oleoresin-paprika-market-analysis-trends | B | 19 nov 2026 |
| 17 | Tridge, oleorresina de paprika | https://www.tridge.com/market-overview/paprika-oleoresin | B | 19 nov 2026 |
| 18 | Tridge, oleorresina de capsicum | https://www.tridge.com/market-overview/capsicum-oleoresin | B | 19 nov 2026 |
| 19 | Pharmaoffer, capsicum | https://pharmaoffer.com/api-excipient-supplier/transactions/capsicum-oleoresin | B | 19 nov 2026 |
| 20 | Tridge, extracto de pimienta negra | https://www.tridge.com/market-overview/black-pepper-extract | B | 19 nov 2026 |
| 21 | IndiaMART, oleorresina de pimienta negra | https://dir.indiamart.com/impcat/black-pepper-oleoresin.html | B | 19 nov 2026 |
| 22 | ExportersIndia, oleorresinas | https://www.exportersindia.com/indian-suppliers/oleoresin.htm | B | 19 nov 2026 |
| 23 | Commodity Board, semilla de apio FOB Nueva Delhi | https://commodity-board.com/indian-celery-seed-fob-new-delhi-edges-higher-on-firm-export-interest | B | 19 nov 2026 |
| 24 | A. Fakhry & Co., World Perfumery Congress 2025 | https://app.swapcard.com/event/perfumerycongress25/exhibitor/RXhoaWJpdG9yXzIwNjY1OTQ= | B | 19 nov 2026 |
| 25 | Hashem Brothers, Pacto Mundial de la ONU | https://unglobalcompact.org/what-is-gc/participants/4768-Hashem-Brothers-for-Essential-Oils-and-Aromatic-Products | B | 19 nov 2026 |
| 26 | Hashem Brothers, Fair for Life | https://www.fairforlife.org/en/partenaire/hashem-brothers-for-essential-oils-aromatic-products-2/ | B | 19 nov 2026 |
| 27 | Fridal Egypt | http://www.fridalegypt.com/en/essential-oils | B | 19 nov 2026 |
| 28 | Al Sheikh for Export | https://alsheikhforexport.com/products/index.html | B | 19 nov 2026 |
| 29 | Ultra International, aceite de comino de Egipto | https://ultranl.com/products/cumin-seed-oil-egypt/ | B | 19 nov 2026 |
| 30 | Robertet Matières Premières, aceite de comino | https://matieres-premieres.robertet.com/cumin-oil | B | 19 nov 2026 |

---

## Lo que sigue sin verificar

1. **Nombres de importadores egipcios de oleorresinas** en un registro aduanero que se pueda abrir. Givaudan Egypt SAE y Symrise SAE aparecen solo en el resumen del buscador sobre Volza. Namaa y AFF son compradores plausibles sin prueba de compra.
2. **Arancel egipcio para 3301.90 y para 3203.00** (colorantes de origen vegetal), y si hay recargos además del IVA de 14%.
3. **Si el arancel nacional egipcio subdivide 3301.90** a 10 dígitos y separa oleorresinas.
4. Contenido de la **enmienda de 2026 a la IN 211/2023** de la NFSA. Si paprika (E160c) y cúrcuma/curcumina (E100) siguen en la lista positiva y con qué límites.
5. Si el **Decreto 43/2016** alcanza a ingredientes a granel. Si se exige **halal** para oleorresinas sin declaración halal.
6. Norma de **etiquetado** egipcia aplicable a ingredientes industriales a granel.
7. **Precios 2026** con la página abierta, para todos los productos. **No hay ningún precio 2026 de oleorresina de apio, comino o cilantro**, ni siquiera como pista.
8. **Capacidad y certificados** de cualquier destilador o extractor egipcio. No hay productor egipcio de oleorresina de paprika, capsicum, pimienta, cúrcuma o apio con evidencia.
9. **Desglose por oleorresina** del comercio India→Egipto y China→Egipto (datos espejo por línea nacional, sección 5). Hace falta volver a consultar Comtrade cuando haya créditos.
10. **Exportaciones egipcias de HS 330190 en 2025.**

### Bloqueos técnicos de la sesión

- Hay que habilitar en la red de la sesión, o en WebFetch, al menos estos hosts: comtradeapi.un.org, customs.gov.eg, nfsa.gov.eg, wits.worldbank.org, trade.gov, gomruky.com, volza.com e indianspices.com.
- Los créditos de Firecrawl se agotaron durante la sesión.
