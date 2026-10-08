# INVESTIGACIÓN — Vídeo 006: LA FACTURA DE LA LUZ
### «Por qué tu factura de la luz sube aunque la energía baja»

Fecha de la investigación: 8/10/2026. Fuente principal: **Eurostat, conjunto «Electricity prices components for household consumers – annual data» (nrg_pc_204_c)**, actualizado el 7/10/2026, descargado por la API oficial (JSON en esta carpeta: `fuentes_eurostat_*.json`). Precios en euros por kWh de un hogar, **con todos los impuestos** (los no recuperables para el hogar). Datos de España, 2023–2025, «todas las bandas de consumo» (TOT_KWH).
El canal EXPLICA: nada de esto es una recomendación de contratación.

**Leyenda:** **D** = dato directo de fuente oficial · **C** = cálculo propio con datos D · **!** = dudoso o no confirmado.

## 1. EL REPARTO DE CADA EURO (Eurostat, España, 2025) [D + C]
| Componente (nombre Eurostat) | €/kWh | % del total [C] |
|---|---|---|
| Energía y suministro (Energy and supply) | 0,1159 | 40,8 % |
| Costes de red (Network costs) | 0,0806 | 28,4 % |
| Impuestos, tasas, gravámenes y cargos (Taxes, fees, levies and charges) | 0,0873 | 30,8 % |
| · de ellos, IVA (VAT) | 0,0478 | 16,8 % |
| · de ellos, el resto (impuesto eléctrico, cargos…) [C] | 0,0395 | 13,9 % |
| **Total** [C] | **0,2838** | 100 % |

## 2. LA EVOLUCIÓN (España, €/kWh) [D + C]
| | 2023 | 2024 | 2025 | 2023→2025 |
|---|---|---|---|---|
| Energía y suministro | 0,1349 | 0,1170 | 0,1159 | −14 % |
| Costes de red | 0,0926 | 0,0823 | 0,0806 | −13 % |
| Impuestos, tasas y cargos | 0,0327 | 0,0633 | 0,0873 | **×2,7 (+167 %)** |
| · IVA | 0,0160 | 0,0312 | 0,0478 | ×3,0 |
| **Total** | 0,2602 | 0,2626 | 0,2838 | +9 % |

## 3. COMPARACIÓN CON EUROPA (2025, total €/kWh, todas las bandas) [D]
UE-27: 0,2935 (energía 0,1277; red 0,0836; impuestos 0,0822 = 28,0 %) · Alemania 0,4023 · Italia 0,3512 · Portugal 0,2563 · Francia 0,2546 · **España 0,2838** (impuestos 30,8 %). España está **por debajo de la media de la UE** en precio total y **por encima** en la parte de impuestos y cargos (30,8 % frente a 28,0 %). Precios nominales, sin ajustar por poder adquisitivo.

## 4. LOS COSTES DEL SISTEMA (cargos) EN 2026 [D]
Memoria de la Orden TED/1524/2025 (MITECO, 2/12/2025): «El importe total de los costes del sistema eléctrico asciende a 8.510.447.000 €, mientras que los ingresos destinados a compensar estos cargos ascienden a unos 4.453.023.000 €, fundamentalmente provenientes de las figuras impositivas de la Ley 15/2012… y de las subastas de derechos de emisión de CO2, lo que dejaría un importe de cargos netos a financiar por los consumidores en 2026 de 4.057.424.000 €.» Cálculo: 4.057 / 8.510 = 47,7 % lo pagan los consumidores; 52,3 %, impuestos a la generación y subastas de CO₂. Del ingreso externo, el IVPEE aporta 1.994.696 miles de € y el CO₂, 1.100.000 miles de €. BOE-A-2025-26705 (Orden TED/1524/2025, de 23 de diciembre).

## 5. IMPUESTOS Y SUS RETIRADAS [D]
- IVA general: 21 % (Ley 37/1992, art. 90). IVA de la luz en 2024 (RDL 8/2023, art. 21): **10 %** para contratos ≤ 10 kW cuando el precio medio del mercado diario del mes anterior supera 45 €/MWh (y para vulnerables severos). En 2025: tipo general.
- Impuesto especial sobre la electricidad (IEE): tipo general **5,11269632 %** (Ley 38/1992, art. 99.1). En 2024: **2,5 %** de enero a marzo y **3,8 %** de abril a junio (RDL 8/2023, art. 22).
- ! No se afirma aquí el tipo del IVA ni del IEE de 2023: no se ha verificado en el BOE en esta investigación; solo se dice que los datos de 2023 reflejan las rebajas fiscales de la crisis energética [afirmación general, consistente con los datos de IVA de Eurostat: 0,016 €/kWh sobre 0,26 = 6 %].

## 6. LO QUE NO SE PUEDE AFIRMAR (!)
- Eurostat es una **media** de hogares: tu factura depende de tu tarifa, tu potencia y tu consumo.
- «Impuestos, tasas, gravámenes y cargos» es la categoría de Eurostat; agrupa IVA, impuesto eléctrico y otros gravámenes/cargos. No se desglosa aquí cuánto es cada uno salvo el IVA.
- 2026 aún no está publicado (los datos anuales de 2025 salieron el 7/10/2026).
- No decir «la luz en España es la más cara de Europa»: en 2025 España está por debajo de la media de la UE-27 en el total.
