semantics_dict = {
    "id": "id",
    "age": "continuous",
    "death": "outcome",           # death by NDI follow-up (post-admission outcome)
    "sex": "categorical",
    "hospdead": "outcome",        # in-hospital death (post-admission outcome)
    "slos": "target",             # hospital length of stay (days)
    "d.time": "outcome",          # days of follow-up (time-to-event/censoring)
    "dzgroup": "categorical",     # 9-level disease subgroup
    "dzclass": "categorical",     # 4-level disease class
    "num.co": "ordinal",          # number of comorbidities (count; treat as ordinal/continuous)
    "edu": "continuous",          # years of education
    "income": "categorical",      # 4-level income bracket
    "scoma": "score",             # SUPPORT coma score (based on Glasgow)
    "charges": "cost",
    "totcst": "cost",
    "totmcst": "cost",
    "avtisst": "score",           # Average TISS (days 3–25)
    "race": "categorical",        # 5-level race/ethnicity
    "sps": "score",               # SUPPORT physiology score (day 3)
    "aps": "score",               # APS III (day 3)
    "surv2m": "prognostic_day3",  # model survival prediction at day 3 (derived)
    "surv6m": "prognostic_day3",  # model survival prediction at day 3 (derived)
    "hday": "continuous",         # hospital day at study admit
    "diabetes": "categorical",    # comorbidity indicator
    "dementia": "categorical",    # comorbidity indicator
    "ca": "categorical",          # cancer status: no/yes/metastatic
    "prg2m": "clinician_estimate",# MD 2-month survival estimate (subjective)
    "prg6m": "clinician_estimate",# MD 6-month survival estimate (subjective)
    "dnr": "policy",              # DNR status (no/before/after study admit)
    "dnrday": "policy_time",      # days to DNR (neg = before study)
    "meanbp": "physio_day3",      # mean arterial blood pressure (day 3)
    "wblc": "physio_day3",        # white blood cell count (day 3)
    "hrt": "physio_day3",         # heart rate (day 3)
    "resp": "physio_day3",        # respiration rate (day 3)
    "temp": "physio_day3",        # temperature C (day 3)
    "pafi": "physio_day3",        # PaO2/(0.01*FiO2) (day 3)
    "alb": "physio_day3",         # serum albumin (day 3)
    "bili": "physio_day3",        # bilirubin (day 3)
    "crea": "physio_day3",        # serum creatinine (day 3)
    "sod": "physio_day3",         # sodium (day 3)
    "ph": "physio_day3",          # arterial pH (day 3)
    "glucose": "physio_day3",     # glucose (day 3)
    "bun": "physio_day3",         # blood urea nitrogen (day 3)
    "urine": "physio_day3",       # urine output (day 3)
    "adlp": "function_score",     # activities of daily living: patient (day 3)
    "adls": "function_score",     # ADL surrogate (day 3)
    "sfdm2": "outcome",           # functional disability at 2 months (5-level outcome)
    "adlsc": "function_score"     # imputed ADL calibrated to surrogate
}

description_dict = {
    "id": "Patient identifier.",
    "age": "Age in years at study entry.",
    "death": "Death at any time up to National Death Index (NDI) date 31-Dec-1994.",
    "sex": "Sex of patient (male/female).",
    "hospdead": "Death in hospital during index stay.",
    "slos": "Days from study entry to discharge (length of stay).",
    "d.time": "Days of follow-up from study entry.",
    "dzgroup": "Disease subgroup: ARF/MOSF w/Sepsis, COPD, CHF, Cirrhosis, Coma, Colon Cancer, Lung Cancer, MOSF w/Malignancy.",
    "dzclass": "Disease class: ARF/MOSF; COPD/CHF/Cirrhosis; Coma; Cancer.",
    "num.co": "Number of comorbid conditions.",
    "edu": "Years of formal education.",
    "income": "Household income bracket (under $11k; $11–$25k; $25–$50k; >$50k).",
    "scoma": "SUPPORT coma score based on Glasgow (Day 3).",
    "charges": "Hospital charges for the stay.",
    "totcst": "Total RCC cost.",
    "totmcst": "Total micro-cost.",
    "avtisst": "Average Therapeutic Intervention Scoring System (TISS), Days 3–25.",
    "race": "Race/ethnicity (white, black, asian, other, hispanic).",
    "sps": "SUPPORT physiology score (Day 3).",
    "aps": "APS III (no coma; adjustments per study) (Day 3).",
    "surv2m": "Model-predicted 2-month survival at Day 3.",
    "surv6m": "Model-predicted 6-month survival at Day 3.",
    "hday": "Hospital day at study admission.",
    "diabetes": "Diabetes comorbidity indicator.",
    "dementia": "Dementia comorbidity indicator.",
    "ca": "Cancer status (no/yes/metastatic).",
    "prg2m": "Physician’s 2-month survival estimate (subjective).",
    "prg6m": "Physician’s 6-month survival estimate (subjective).",
    "dnr": "Do-Not-Resuscitate status (no DNR; DNR before study admit; DNR after study admit).",
    "dnrday": "Days to DNR order (negative if before study entry).",
    "meanbp": "Mean arterial blood pressure (Day 3).",
    "wblc": "White blood cell count (Day 3).",
    "hrt": "Heart rate (Day 3).",
    "resp": "Respiratory rate (Day 3).",
    "temp": "Temperature in Celsius (Day 3).",
    "pafi": "PaO2/(0.01×FiO2) ratio (Day 3).",
    "alb": "Serum albumin (Day 3).",
    "bili": "Serum bilirubin (Day 3).",
    "crea": "Serum creatinine (Day 3).",
    "sod": "Serum sodium (Day 3).",
    "ph": "Arterial pH (Day 3).",
    "glucose": "Serum glucose (Day 3).",
    "bun": "Blood urea nitrogen (Day 3).",
    "urine": "Urine output (Day 3).",
    "adlp": "Activities of daily living score (patient self-report, Day 3).",
    "adls": "Activities of daily living score (surrogate, Day 3).",
    "sfdm2": "Functional disability at 2 months (5-level scale).",
    "adlsc": "Imputed ADL calibrated to surrogate."
}

ethical_dict = {
    "id": "no",
    "age": "yes",        # age is sensitive for fairness considerations
    "death": "yes",      # mortality outcome is highly sensitive
    "sex": "yes",
    "hospdead": "yes",
    "slos": "no",
    "d.time": "yes",
    "dzgroup": "no",
    "dzclass": "no",
    "num.co": "no",
    "edu": "yes",        # socioeconomic / education
    "income": "yes",     # socioeconomic / income
    "scoma": "yes",      # neurological/mental status implication
    "charges": "yes",    # financial/cost data
    "totcst": "yes",
    "totmcst": "yes",
    "avtisst": "no",
    "race": "yes",       # protected attribute
    "sps": "no",
    "aps": "no",
    "surv2m": "yes",     # prognostic values; sensitive outcome-related
    "surv6m": "yes",
    "hday": "no",
    "diabetes": "yes",   # health condition
    "dementia": "yes",   # mental/cognitive health
    "ca": "yes",         # cancer status
    "prg2m": "yes",      # clinician judgment about survival
    "prg6m": "yes",
    "dnr": "yes",        # end-of-life preference/order
    "dnrday": "yes",
    "meanbp": "no",
    "wblc": "no",
    "hrt": "no",
    "resp": "no",
    "temp": "no",
    "pafi": "no",
    "alb": "no",
    "bili": "no",
    "crea": "no",
    "sod": "no",
    "ph": "no",
    "glucose": "no",
    "bun": "no",
    "urine": "no",
    "adlp": "yes",       # functional status
    "adls": "yes",       # functional status (surrogate)
    "sfdm2": "yes",      # disability/mortality at 2 months
    "adlsc": "yes"       # imputed functional status
}

units_dict = {
    # Outcomes / time-to-event
    "slos": "days",                      # study entry → discharge (length of stay)
    "d.time": "days",                    # days of follow-up from study entry
    "death": "binary indicator",         # 0/1 death during follow-up
    "hospdead": "binary indicator",      # 0/1 death in hospital during index stay
    "sfdm2": "ordinal score (1–5)",      # functional disability category at 2 months

    # Costs
    "charges": "US dollars",             # hospital charges for stay
    "totcst": "US dollars",              # total RCC cost
    "totmcst": "US dollars",             # total micro-cost

    # IDs & demographics / categorical
    "id": "identifier",                  # patient ID (no physical unit)
    "ca": "categorical (cancer status)", # no/yes/metastatic
    "dementia": "binary indicator",      # 0/1 comorbidity
    "diabetes": "binary indicator",      # 0/1 comorbidity
    "dzclass": "categorical (disease class)",
    "dzgroup": "categorical (disease subgroup)",
    "income": "ordinal income bracket",  # income category
    "race": "categorical (race/ethnicity)",
    "sex": "categorical (sex)",
    "num.co": "count",                   # number of comorbid conditions

    # Baseline continuous demographics / time
    "age": "years",                      # age at study entry
    "edu": "years",                      # years of formal education
    "hday": "days",                      # hospital day of study admit

    # Scores
    "aps": "APACHE III score (dimensionless)",
    "avtisst": "TISS score (dimensionless)",
    "scoma": "SUPPORT coma score (dimensionless)",
    "sps": "SUPPORT physiology score (dimensionless)",

    # Lab / physiologic day 3
    "alb": "g/dL",                       # serum albumin
    "bili": "mg/dL",                     # serum bilirubin
    "bun": "mg/dL",                      # blood urea nitrogen
    "crea": "mg/dL",                     # serum creatinine
    "glucose": "mg/dL",                  # serum glucose
    "hrt": "beats/min",                  # heart rate
    "meanbp": "mmHg",                    # mean arterial blood pressure
    "pafi": "mmHg",                      # PaO2/(0.01×FiO2) ratio (pressure)
    "ph": "dimensionless (pH)",          # logarithmic hydrogen ion concentration
    "resp": "breaths/min",               # respiratory rate
    "sod": "mEq/L",                      # serum sodium concentration
    "temp": "°C",                        # body temperature
    "urine": "mL/day",                   # urine output per 24h
    "wblc": "10^3 cells/µL",             # white blood count (thousands)

    # Function / ADL scores
    "adlp": "ADL score (patient, dimensionless)",
    "adls": "ADL score (surrogate, dimensionless)",
    "adlsc": "ADL score (calibrated, dimensionless)",

    # Prognostic model outputs / probabilities
    "surv2m": "probability (0–1)",       # SUPPORT model 2-month survival estimate
    "surv6m": "probability (0–1)",       # SUPPORT model 6-month survival estimate
    "prg2m": "probability (0–1)",        # physician 2-month survival estimate
    "prg6m": "probability (0–1)",        # physician 6-month survival estimate

    # Policy variables
    "dnr": "categorical (code for DNR status)",
    "dnrday": "days",                    # days to DNR order (negative if before study entry)
}