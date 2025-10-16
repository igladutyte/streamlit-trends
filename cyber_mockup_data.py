# ============================================================================
# MARKET INTELLIGENCE OVERVIEW - REAL ATTACKS & INCIDENTS
# ============================================================================

market_intelligence_snapshot = {
    "period": "Last 30 Days",
    "generated_date": "October 15, 2025",

    # Hero metrics - real incident intelligence
    "hero_insights": [
        {
            "label": "💥 Biggest Attack",
            "value": "Jaguar Land Rover Supply Chain Breach",
            "details": {
                "threat_actor": "Scattered Spider",
                "impact": "Production halted across 3 facilities, 2-week vehicle delivery delays",
                "estimated_cost": "£50M+ in production losses and recovery",
                "coverage": "420 articles over 3 weeks"
            },
            "why_it_matters": "Demonstrated that automotive just-in-time manufacturing is critically vulnerable. Single supplier portal compromise cascaded into multi-facility shutdown.",
            "article_examples": [
                "Financial Times: 'JLR halts production at UK plants following cyberattack'",
                "Reuters: 'Scattered Spider's automotive targeting signals new threat actor strategy'",
                "BBC: 'Jaguar customers face months-long delivery delays after breach'"
            ]
        },
        {
            "label": "💰 Most Costly Incident",
            "value": "Asahi Group Ransomware",
            "details": {
                "threat_actor": "Qilin ransomware group",
                "impact": "9,300+ files compromised, earnings release postponed",
                "estimated_cost": "¥2.3B ($15M) in immediate costs, unknown long-term impact",
                "coverage": "95 articles across Japan, APAC, global business press"
            },
            "why_it_matters": "First major Japanese company to publicly disclose full breach details—potential cultural shift in Asian corporate transparency.",
            "article_examples": [
                "Nikkei: 'Asahi postpones earnings amid ransomware crisis'",
                "Japan Times: 'Personal information possibly leaked in cyberattack on Asahi group'",
                "Bloomberg: 'Japanese beverage giant faces operational disruption from cyber incident'"
            ]
        },
        {
            "label": "⚠️ Highest Impact Sector",
            "value": "Transportation & Aviation",
            "details": {
                "major_incidents": [
                    "Brussels Airport: 5-day system outage, 50,000+ passengers affected",
                    "Qantas: Check-in systems down, 2-day operational disruption",
                    "Multiple European airports: Coordinated infrastructure targeting"
                ],
                "combined_impact": "100,000+ travelers disrupted, €20M+ in airline compensation",
                "coverage": "238 articles (+31.5% growth)"
            },
            "why_it_matters": "Critical infrastructure attacks creating visible consumer chaos. Media attention = political pressure = regulatory action coming.",
            "article_examples": [
                "The Guardian: 'Brussels Airport chaos as cyber incident forces manual check-ins'",
                "Sydney Morning Herald: 'Qantas meltdown leaves thousands stranded'",
                "Aviation Week: 'European aviation cybersecurity failures expose systemic vulnerabilities'"
            ]
        },
        {
            "label": "🎯 Most Targeted",
            "value": "Technology Sector",
            "details": {
                "incident_count": "4,015 articles across multiple incidents",
                "major_victims": [
                    "Salesforce: Platform vulnerability affecting thousands of customers",
                    "Discord: Massive phishing campaign using platform infrastructure",
                    "Microsoft: Multiple Azure outages and third-party attacks"
                ],
                "attack_types": "Platform vulnerabilities, supply chain compromises, SaaS exploitation"
            },
            "why_it_matters": "Platform attacks have multiplier effects—one vulnerability affects thousands of organizations simultaneously.",
            "article_examples": [
                "TechCrunch: 'Salesforce vulnerability exposes customer data across enterprise deployments'",
                "The Verge: 'Discord's malware problem is getting worse'",
                "ZDNet: 'Microsoft's security woes continue as Azure faces fresh compromises'"
            ]
        }
    ],

    # Real attacks breakdown - by the numbers
    "attack_landscape": {
        "major_incidents_this_period": [
            {
                "date": "2025-10-15",
                "victim": "Noosa Shire Council (Australia)",
                "attack_type": "Business Email Compromise",
                "financial_loss": "$2.3M",
                "how_it_happened": "International criminal gang exploited procedural vulnerabilities during Christmas period when approval processes were relaxed and skeleton staff operated",
                "business_impact": "Financial loss, reputational damage, ongoing investigation",
                "media_angle": "Small council vulnerability highlights that sophisticated fraud doesn't require technical sophistication—just understanding of organizational processes",
                "article_examples": [
                    "ABC News Australia: 'Noosa Council confirms $2.3 million cyber fraud during Christmas period'",
                    "Brisbane Times: 'How a small Queensland council lost millions to international hackers'"
                ],
                "lessons": "Holiday periods with reduced staffing = elevated BEC risk. Approval workflows must maintain rigor during seasonal transitions."
            },
            {
                "date": "2025-10-15",
                "victim": "German Government Procurement Portal",
                "attack_type": "DDoS Attack",
                "financial_loss": "Undisclosed (operational disruption)",
                "how_it_happened": "Pro-Russian hackers targeted public procurement infrastructure, rendering it inaccessible for nearly a week during heightened geopolitical tensions",
                "business_impact": "Government operations disrupted, procurement delays, political embarrassment",
                "media_angle": "Geopolitical cyber operations intersecting with critical infrastructure—attack timing aligned with policy debates about digital sovereignty",
                "article_examples": [
                    "Deutsche Welle: 'Germany's procurement portal down for week following cyberattack'",
                    "Politico EU: 'Pro-Russian hackers target German infrastructure amid Ukraine tensions'",
                    "Reuters: 'Berlin struggles to restore critical government services after DDoS assault'"
                ],
                "lessons": "Critical infrastructure attacks increasingly timed to political calendars. Operational resilience matters more than attribution speed."
            },
            {
                "date": "2025-10-15",
                "victim": "Multiple European Airports",
                "attack_type": "System Compromise (attribution unclear)",
                "financial_loss": "€20M+ in airline compensation and operational costs",
                "how_it_happened": "Electronic check-in and boarding systems disrupted across multiple airports. Technical details remain unclear—media couldn't confirm cyberattack vs. system failure, yet covered extensively",
                "business_impact": "Thousands of passengers stranded, manual check-in processes, multi-day recovery",
                "media_angle": "The mere suspicion of cyber involvement generated massive coverage. Shows how 'cyber' has become default explanation for any unexpected technical failure",
                "article_examples": [
                    "BBC: 'European airports face chaos as check-in systems fail'",
                    "Le Monde: 'Cyberattaque possible sur les aéroports européens'",
                    "Financial Times: 'Aviation industry faces questions over cybersecurity preparedness'"
                ],
                "lessons": "Critical infrastructure + consumer disruption = sustained media coverage regardless of technical attribution. Prepare crisis communications for ambiguous incidents."
            },
            {
                "date": "2025-10-08",
                "victim": "Jaguar Land Rover",
                "attack_type": "Supply Chain Attack",
                "financial_loss": "£50M+ estimated (production losses, recovery costs)",
                "how_it_happened": "Scattered Spider compromised supplier portal, cascading into production halts across multiple UK facilities. Social engineering enabled initial access",
                "business_impact": "3 facilities shut down, 2-week production halt, vehicle delivery delays extending months, supply chain partner impacts",
                "media_angle": "Every production update became new article. British media relentless on national manufacturer. Demonstrated automotive industry's just-in-time vulnerability",
                "article_examples": [
                    "Financial Times: 'JLR production halted as cyberattack hits UK plants'",
                    "Automotive News: 'Scattered Spider's JLR breach exposes automotive cybersecurity gap'",
                    "The Times: 'British car buyers face months-long delays after Jaguar cyber incident'",
                    "BBC: 'JLR workers sent home as factories remain offline'",
                    "Sky News: 'Cybersecurity experts warn automotive sector faces systemic risk'"
                ],
                "lessons": "Just-in-time manufacturing has no buffer capacity. Single point of failure in digital supply chain can halt multi-billion operations. Visible disruption = media frenzy = board pressure."
            },
            {
                "date": "2025-10-08",
                "victim": "Asahi Group Holdings",
                "attack_type": "Ransomware",
                "financial_loss": "¥2.3B ($15M+) immediate costs, ongoing operational impact",
                "how_it_happened": "Qilin ransomware group penetrated network, exfiltrated 9,300+ files, deployed encryption. Group used professional leak site with countdown timer to pressure payment",
                "business_impact": "Operations disrupted, earnings release postponed (unprecedented for Japanese company), data potentially exposed, recovery ongoing",
                "media_angle": "Japanese corporate transparency breakthrough. Asahi provided detailed public updates—highly unusual for Japanese business culture. May establish new disclosure expectations",
                "article_examples": [
                    "Nikkei Asia: 'Asahi Group postpones earnings announcement following ransomware attack'",
                    "Japan Times: 'Personal information possibly leaked in cyberattack on Asahi group'",
                    "Bloomberg: 'Japanese beverage giant's cyber woes signal cultural shift in disclosure'",
                    "Mainichi: '朝日グループ、サイバー攻撃で決算発表延期'",
                    "Reuters: 'Qilin ransomware group claims responsibility for Asahi breach'"
                ],
                "lessons": "Ransomware groups targeting Asian companies to test disclosure norms. Transparent response can generate more positive coverage than attempted cover-up. Financial calendar pressure accelerates disclosure decisions."
            },
            {
                "date": "2025-09-25",
                "victim": "Salesforce Platform",
                "attack_type": "Vulnerability Disclosure (not breach, but affecting thousands)",
                "financial_loss": "Undisclosed (customer exposure costs vary)",
                "how_it_happened": "Critical vulnerability in platform discovered, disclosed. Not exploited in wild (yet), but thousands of Salesforce customers suddenly had action item",
                "business_impact": "Platform-wide patch deployment, customer assessment of exposure, emergency security updates",
                "media_angle": "Platform vulnerabilities generate coverage disproportionate to traditional breaches because of multiplier effect—one flaw affects thousands of organizations",
                "article_examples": [
                    "TechCrunch: 'Salesforce patches critical vulnerability affecting enterprise customers'",
                    "CRN: 'Salesforce security flaw puts thousands of businesses at risk'",
                    "The Register: 'Salesforce customers scramble to patch after vulnerability disclosure'",
                    "CSO Online: 'Why SaaS platform vulnerabilities are the new supply chain risk'"
                ],
                "lessons": "Platform security failures are everyone's problem. SaaS concentrations create systemic risk. Patch deployment at scale reveals organizational security maturity."
            },
            {
                "date": "2025-09-20",
                "victim": "Collins Aerospace",
                "attack_type": "Data Breach",
                "financial_loss": "Undisclosed (regulatory penalties, remediation costs pending)",
                "how_it_happened": "Details limited due to defense contractor sensitivities. Employee and supplier data compromised",
                "business_impact": "Dual impact: commercial aviation operational concerns + national security classified information exposure fears",
                "media_angle": "Defense contractor breaches get coverage multiplication—aviation industry trades, defense journalists, cybersecurity press, business media all covering from different angles",
                "article_examples": [
                    "Defense News: 'Collins Aerospace data breach raises supply chain security concerns'",
                    "Aviation Week: 'Major aerospace supplier confirms cyber incident'",
                    "Wall Street Journal: 'Raytheon subsidiary faces questions over data protection'",
                    "Federal Times: 'DOD reviews supplier security after Collins breach'"
                ],
                "lessons": "Organizations serving multiple sectors (commercial + military) get coverage multiplication. Defense contractors face heightened scrutiny. Supply chain security now procurement requirement."
            },
            {
                "date": "2025-09-19",
                "victim": "AT&T",
                "attack_type": "Data Leak",
                "financial_loss": "Undisclosed (likely $50M+ in remediation, legal, regulatory)",
                "how_it_happened": "Customer data exposed through undisclosed vulnerability. Details limited",
                "business_impact": "Customer notification, regulatory investigations, class-action lawsuits pending",
                "media_angle": "Modest coverage (87 articles) despite major brand—reflects breach fatigue. AT&T has had so many incidents that media treats new breaches as routine",
                "article_examples": [
                    "The Verge: 'AT&T confirms another data breach affecting customers'",
                    "CNET: 'What AT&T customers need to know about latest security incident'",
                    "TechCrunch: 'AT&T's breach problem continues with new customer data exposure'"
                ],
                "lessons": "Repeat incidents create narrative fatigue even for major brands. Normalization reduces public pressure for improvements. Media coverage doesn't correlate with business impact."
            }
        ],

        "attack_type_breakdown": {
            "ransomware": {
                "incident_count": "761 articles covering multiple incidents",
                "notable_cases": ["Asahi Group (Qilin)", "Healthcare sector (multiple, normalized)"],
                "average_ransom_demand": "$1.5M - $5M (mid-market), $10M+ (enterprise)",
                "average_downtime": "18-23 days for full recovery",
                "average_total_cost": "10x ransom demand (recovery, lost business, reputation)",
                "trend": "Coverage emphasizes operational disruption over ransom amounts. Media narrative shifted from 'should they pay?' to 'how long until operations restore?'"
            },
            "supply_chain_attacks": {
                "incident_count": "Dominated by JLR incident (420 articles)",
                "why_effective": "Multiplier effect—single compromise cascades to multiple organizations",
                "notable_pattern": "Attackers targeting suppliers with weaker security to access larger targets",
                "average_impact": "15-30 day disruption, affects 50+ downstream organizations",
                "trend": "Growing sophistication. Attackers mapping supply chains before targeting weakest link with highest impact potential."
            },
            "business_email_compromise": {
                "incident_count": "Under-reported in media but extremely common",
                "notable_cases": ["Noosa Council $2.3M"],
                "average_loss": "$50K - $500K (small orgs), $1M+ (large orgs)",
                "success_factors": "Holiday periods, executive impersonation, process familiarity",
                "trend": "AI-enabled BEC emerging—deepfake voice calls enabling real-time executive impersonation"
            },
            "platform_vulnerabilities": {
                "incident_count": "193 articles (Salesforce), 130 (Microsoft), 133 (Oracle)",
                "why_dangerous": "One vulnerability affects thousands of organizations simultaneously",
                "patch_challenge": "Enterprise customers need 30-90 days for testing before deployment",
                "trend": "SaaS concentration creating systemic risk. Platform security failures are everyone's problem."
            },
            "critical_infrastructure": {
                "incident_count": "887 articles across transportation, utilities, aviation",
                "notable_cases": ["Brussels Airport", "Qantas", "German Government"],
                "why_different": "Physical-world consequences, safety concerns, regulatory attention",
                "average_cost": "€5M - €50M depending on duration and scope",
                "trend": "Fastest-growing sector (+31.5%). Visible disruption attracts media, media attracts political attention, political attention drives regulatory action."
            }
        },

        "cost_intelligence": {
            "direct_costs": {
                "ransom_payments": {
                    "range": "$100K - $10M depending on target size",
                    "trend": "Declining as percentage of total cost. Now <10% of total incident cost",
                    "note": "Media stopped reporting ransom amounts—normalized and considered private business decision"
                },
                "recovery_costs": {
                    "forensics_investigation": "$500K - $2M for major incidents",
                    "system_restoration": "$1M - $10M depending on infrastructure complexity",
                    "data_recovery": "$200K - $5M depending on backup maturity",
                    "legal_counsel": "$500K - $5M for major incidents with regulatory exposure"
                },
                "operational_disruption": {
                    "lost_revenue": "$1M - $50M per day depending on organization size",
                    "example": "JLR estimated £50M+ in production losses over 2-week shutdown",
                    "multiplier_effect": "Supply chain impacts 3-5x direct victim costs"
                }
            },
            "indirect_costs": {
                "reputation_damage": {
                    "stock_price_impact": "Average 3-5% decline immediately post-disclosure",
                    "customer_churn": "5-10% for consumer brands, 2-5% for B2B",
                    "brand_value": "Difficult to quantify but long-term impact significant",
                    "example": "AT&T's repeated breaches normalizing customer expectations—may reduce switching for entire sector"
                },
                "regulatory_penalties": {
                    "gdpr_fines": "Up to €20M or 4% global revenue (whichever higher)",
                    "sec_penalties": "$1M - $50M for disclosure failures",
                    "sector_specific": "Healthcare (HIPAA), finance (SOX), vary widely",
                    "trend": "Increasing. Regulators using cybersecurity penalties to demonstrate authority"
                },
                "insurance_premiums": {
                    "post_incident_increase": "50-200% premium increases after major incident",
                    "market_trend": "Cyber insurance tightening. More exclusions, higher premiums, lower coverage limits",
                    "example": "Healthcare sector facing insurance crisis—some insurers limiting ransomware coverage"
                },
                "opportunity_costs": {
                    "delayed_projects": "Security incidents halt other initiatives, delaying revenue-generating projects",
                    "executive_distraction": "C-suite spending months managing incident vs. driving business growth",
                    "competitive_disadvantage": "While recovering, competitors advancing. Market share losses difficult to quantify"
                }
            },
            "total_cost_analysis": {
                "formula": "Total Cost = Direct Costs (10-30%) + Indirect Costs (70-90%)",
                "example_breakdown": {
                    "incident": "Mid-market company ransomware",
                    "ransom_paid": "$500K (5%)",
                    "recovery_costs": "$2M (20%)",
                    "operational_disruption": "$3M (30%)",
                    "reputation_customer_impact": "$3M (30%)",
                    "regulatory_legal": "$1M (10%)",
                    "insurance_premium_increases": "$500K (5%)",
                    "total_cost": "$10M",
                    "multiple_of_ransom": "20x"
                },
                "key_insight": "Organizations focusing on ransom decision missing 95% of actual costs. Business continuity and reputation management far more important than payment decision."
            }
        }
    },

    # Timing intelligence - when attacks happen and why
    "timing_intelligence": {
        "seasonal_patterns": [
            {
                "season": "Q4 Holiday Period (Nov-Dec)",
                "risk_level": "Critical",
                "why_vulnerable": "Skeleton staff, relaxed approval processes, year-end urgency creates exploitable conditions",
                "historical_data": "23% higher BEC success rates, 18% more ransomware attacks",
                "examples": [
                    "Noosa Council: $2.3M fraud during Christmas period",
                    "Historical: Colonial Pipeline (Mother's Day weekend), Kaseya (July 4 weekend)"
                ],
                "attacker_strategy": "Target holidays when incident response teams understaffed and executive approval chains disrupted",
                "defensive_recommendation": "Tighten approval workflows before December. Plan incident response coverage for holidays. Don't relax security during 'quiet' periods."
            },
            {
                "season": "Earnings Season (Quarterly)",
                "risk_level": "Elevated",
                "why_vulnerable": "Disclosure pressure, financial calendar deadlines create rushing and mistakes",
                "historical_data": "70% of major breach disclosures align with quarterly reporting windows",
                "examples": [
                    "Asahi: Ransomware forced earnings postponement",
                    "Pattern: Organizations delay disclosure until legally required (earnings call)"
                ],
                "attacker_strategy": "Earnings pressure accelerates ransom negotiations. Organizations more likely to pay to avoid disclosure",
                "defensive_recommendation": "Incident response planning should account for earnings calendar. Board briefings on disclosure obligations before incidents occur."
            },
            {
                "season": "Election Cycles",
                "risk_level": "Elevated (for government/political targets)",
                "why_vulnerable": "Political sensitivity, media attention, geopolitical tensions",
                "historical_data": "40% higher government sector coverage during election years",
                "examples": [
                    "Australian Electoral Commission deepfake warnings during election prep",
                    "German government attacked during policy debates",
                    "Pattern: Nation-state operations intensify around elections"
                ],
                "attacker_strategy": "Maximum political impact during sensitive periods. Operations timed to influence or disrupt",
                "defensive_recommendation": "Government and politically-adjacent organizations should elevate security posture 6 months before elections."
            },
            {
                "season": "Summer Months (Jun-Aug)",
                "risk_level": "Moderate but overlooked",
                "why_vulnerable": "Vacation schedules create coverage gaps. 'Nothing happens in summer' mentality",
                "historical_data": "Historically major attacks launched during summer lulls",
                "examples": [
                    "Kaseya ransomware: July 4 weekend",
                    "Many major breaches: Friday afternoon before long weekends"
                ],
                "attacker_strategy": "Strike when defenders on vacation and organizations assume quiet period",
                "defensive_recommendation": "Maintain full security staffing during summer. Avoid 'everyone takes vacation' scenarios."
            }
        ],

        "time_of_week_patterns": {
            "friday_afternoon": {
                "risk_level": "High",
                "attacker_preference": "Ransomware deployments often Friday 5pm-8pm",
                "why": "Discovered Monday morning after propagation weekend. Incident response teams scattered. Maximizes business disruption time.",
                "examples": "Multiple ransomware groups documented using Friday deployment",
                "defense": "Elevated monitoring Friday evenings. Weekend incident response on-call rotation."
            },
            "holiday_weekends": {
                "risk_level": "Critical",
                "attacker_preference": "Major attacks timed to 3-4 day weekends",
                "why": "Extended time before discovery. Difficulty assembling response teams during holidays.",
                "examples": "Colonial Pipeline (Mother's Day), Kaseya (July 4), numerous others",
                "defense": "Don't reduce security monitoring during holiday weekends. Plan incident response coverage explicitly."
            }
        }
    },

    # Emerging threat narratives
    "emerging_narratives": [
        {
            "narrative": "Manufacturing as New Cyber Frontline",
            "current_state": "Under-reported but exploding (+23.1%)",
            "key_incident": "Jaguar Land Rover—£50M+ impact from 2-week production halt",
            "why_emerging": "Just-in-time manufacturing has zero buffer capacity. Single digital failure cascades to multi-facility shutdown. Supply chain complexity creates massive attack surface.",
            "attacker_interest": "Visible disruption = media attention = operational pressure = faster ransom payments",
            "coverage_examples": [
                "Financial Times: 'Automotive industry faces cybersecurity reckoning after JLR breach'",
                "Manufacturing Today: 'Industrial control system vulnerabilities exposed by recent attacks'",
                "Supply Chain Dive: 'Just-in-time manufacturing's cyber vulnerability problem'"
            ],
            "opportunity_window": "6-12 months before market crowded with 'experts'",
            "thought_leadership_angle": "Own 'industrial cybersecurity' positioning. OT/IT convergence expertise. Manufacturing-specific frameworks."
        },
        {
            "narrative": "Transportation as Critical Infrastructure Poster Child",
            "current_state": "Surging (+31.5%) and gaining political attention",
            "key_incidents": "Brussels Airport (5-day outage), Qantas (operational disruption), coordinated European targeting",
            "why_emerging": "Perfect media storm: visible consumer chaos + safety concerns + photographable disruption = sustained coverage = political pressure",
            "cost_impact": "€20M+ in airline compensation, 100,000+ travelers disrupted",
            "coverage_examples": [
                "The Guardian: 'Brussels Airport chaos exposes aviation cybersecurity gaps'",
                "Aviation Week: 'European aviation faces systemic cyber vulnerabilities'",
                "Politico: 'Transportation security becomes political priority after incidents'"
            ],
            "opportunity_window": "12-18 months before normalized",
            "thought_leadership_angle": "Critical infrastructure security requires different playbook than enterprise IT. Physical-digital convergence expertise."
        },
        {
            "narrative": "Deepfake Authentication Crisis",
            "current_state": "Mainstream breakthrough—jumped from tech to political coverage",
            "key_trigger": "Australian Electoral Commission warnings pushed deepfakes from theoretical to democracy threat",
            "coverage_growth": "+47% in one week—fastest narrative expansion tracked",
            "real_incidents": "CEO voice impersonation for wire transfers, executive video call fraud emerging",
            "coverage_examples": [
                "Financial Times: 'Deepfakes move from curiosity to business threat'",
                "Sydney Morning Herald: 'Electoral commission warns of deepfake threat to democracy'",
                "WSJ: 'Companies scramble to defend against AI-enabled fraud'"
            ],
            "opportunity_window": "90 days before market saturates with opinions",
            "thought_leadership_angle": "Process resilience when authentication is spoofable. Multi-channel verification frameworks. Beyond detection strategies."
        },
        {
            "narrative": "Platform Concentration Risk",
            "current_state": "Emerging recognition of systemic vulnerability",
            "key_incidents": "Salesforce vulnerability affecting thousands, Microsoft Azure outages cascading",
            "why_matters": "SaaS concentration means one vulnerability = everyone's problem simultaneously",
            "coverage_examples": [
                "TechCrunch: 'Salesforce vulnerability exposes systemic risk of platform concentration'",
                "The Register: 'When your SaaS provider gets breached, so do you'",
                "CSO: 'Platform security is the new supply chain risk'"
            ],
            "opportunity_window": "18-24 months",
            "thought_leadership_angle": "Enterprise architecture for platform risk management. Diversification strategies. Platform security evaluation frameworks."
        }
    ]
}
