# ============================================================================
# VISUAL DASHBOARD LAYOUT - ENGAGING PRESENTATION
# ============================================================================

visual_dashboard_layout = {

    # ============================================================================
    # SECTION 1: THREAT HEATMAP - VISUAL RISK OVERVIEW
    # ============================================================================
    "threat_heatmap": {
        "title": "30-Day Threat Landscape Heatmap",
        "description": "Real-time intelligence on active threats, costs, and coverage intensity",

        "heatmap_data": [
            {
                "threat_category": "Ransomware",
                "severity": 9.2,
                "coverage_intensity": 761,
                "avg_cost": "$5M-$15M",
                "trend_arrow": "↑",
                "color": "#DC2626",  # Red
                "icon": "🔒",
                "recent_victim": "Asahi Group",
                "impact": "Operations halted, earnings postponed"
            },
            {
                "threat_category": "Supply Chain Attacks",
                "severity": 8.8,
                "coverage_intensity": 420,
                "avg_cost": "£50M+",
                "trend_arrow": "↑↑",
                "color": "#EA580C",  # Orange-Red
                "icon": "🔗",
                "recent_victim": "Jaguar Land Rover",
                "impact": "Multi-facility production halt"
            },
            {
                "threat_category": "Deepfake/AI Threats",
                "severity": 8.5,
                "coverage_intensity": 318,
                "avg_cost": "$500K-$2M per incident",
                "trend_arrow": "↑↑↑",
                "color": "#F59E0B",  # Amber
                "icon": "🎭",
                "recent_victim": "Multiple (emerging)",
                "impact": "Wire fraud, executive impersonation"
            },
            {
                "threat_category": "Critical Infrastructure",
                "severity": 8.7,
                "coverage_intensity": 887,
                "avg_cost": "€5M-€50M",
                "trend_arrow": "↑",
                "color": "#EF4444",  # Red
                "icon": "⚡",
                "recent_victim": "Brussels Airport",
                "impact": "50,000+ passengers disrupted"
            },
            {
                "threat_category": "Platform Vulnerabilities",
                "severity": 7.9,
                "coverage_intensity": 456,
                "avg_cost": "Multiplier effect—thousands affected",
                "trend_arrow": "→",
                "color": "#F97316",  # Orange
                "icon": "☁️",
                "recent_victim": "Salesforce, Microsoft",
                "impact": "Systemic risk across customers"
            },
            {
                "threat_category": "BEC/Social Engineering",
                "severity": 7.2,
                "coverage_intensity": 300,
                "avg_cost": "$50K-$2.3M",
                "trend_arrow": "↑",
                "color": "#FBBF24",  # Yellow
                "icon": "🎣",
                "recent_victim": "Noosa Council",
                "impact": "$2.3M holiday fraud"
            },
            {
                "threat_category": "Data Breaches (Traditional)",
                "severity": 6.5,
                "coverage_intensity": 520,
                "avg_cost": "$1M-$10M",
                "trend_arrow": "→",
                "color": "#FCD34D",  # Light Yellow
                "icon": "📁",
                "recent_victim": "AT&T, Collins Aerospace",
                "impact": "Regulatory penalties, lawsuits"
            }
        ],

        "visualization_type": "heatmap_grid",
        "layout_notes": "Display as colored grid/cards. Larger cards = higher severity. Color intensity = risk level. Include trend arrows prominently."
    },

    # ============================================================================
    # SECTION 2: ATTACK TIMELINE - VISUAL INCIDENT MAP
    # ============================================================================
    "attack_timeline": {
        "title": "Major Incidents Timeline - Last 30 Days",
        "subtitle": "Tracking the most impactful attacks by date, cost, and coverage",

        "timeline_events": [
            {
                "date": "Sep 15",
                "event": "Period Start",
                "type": "marker",
                "icon": "📍"
            },
            {
                "date": "Sep 18",
                "event": "JLR Supply Chain Breach Begins",
                "victim": "Jaguar Land Rover",
                "threat_actor": "Scattered Spider",
                "cost": "£50M+",
                "coverage": "420 articles (sustained 3 weeks)",
                "icon": "🚗",
                "severity": "critical",
                "visual_element": "Large milestone with branching coverage arc"
            },
            {
                "date": "Sep 19",
                "event": "AT&T Data Leak",
                "victim": "AT&T",
                "cost": "$50M+ estimated",
                "coverage": "87 articles (modest—breach fatigue)",
                "icon": "📱",
                "severity": "medium",
                "visual_element": "Small marker—shows normalization"
            },
            {
                "date": "Sep 20",
                "event": "Collins Aerospace Breach",
                "victim": "Collins Aerospace",
                "cost": "Undisclosed",
                "coverage": "361 articles (defense contractor sensitivity)",
                "icon": "✈️",
                "severity": "high",
                "visual_element": "Medium milestone"
            },
            {
                "date": "Sep 22",
                "event": "Ransomware Coverage Peak",
                "note": "Weekly high for ransomware mentions (250 articles)",
                "icon": "📊",
                "severity": "info"
            },
            {
                "date": "Sep 25",
                "event": "Salesforce Vulnerability",
                "victim": "Salesforce Platform",
                "cost": "Multiplier effect across customers",
                "coverage": "193 articles",
                "icon": "☁️",
                "severity": "high",
                "visual_element": "Platform risk indicator"
            },
            {
                "date": "Oct 1",
                "event": "Qantas Operational Disruption",
                "victim": "Qantas",
                "cost": "Operational + compensation costs",
                "coverage": "148 articles",
                "icon": "🛫",
                "severity": "high",
                "visual_element": "Transportation cluster begins"
            },
            {
                "date": "Oct 3",
                "event": "Zero-Day Exploitation Surge",
                "note": "Multiple vendors (Microsoft, Cisco, Oracle) = coverage peak",
                "coverage": "420 articles (daily high)",
                "icon": "🔓",
                "severity": "critical",
                "visual_element": "Coverage spike visualization"
            },
            {
                "date": "Oct 5",
                "event": "Brussels Airport System Outage",
                "victim": "Brussels Airport",
                "cost": "€20M+ (airline compensation)",
                "coverage": "116 articles",
                "impact": "50,000+ passengers",
                "icon": "🏢",
                "severity": "critical",
                "visual_element": "Critical infrastructure marker"
            },
            {
                "date": "Oct 8",
                "event": "Asahi Ransomware Attack",
                "victim": "Asahi Group Holdings",
                "threat_actor": "Qilin",
                "cost": "¥2.3B ($15M+)",
                "coverage": "95 articles",
                "icon": "🍺",
                "severity": "critical",
                "visual_element": "Large milestone—Japanese disclosure breakthrough"
            },
            {
                "date": "Oct 10",
                "event": "Deepfake Coverage Peak",
                "note": "Australian Electoral Commission warnings = 43 articles in single day",
                "icon": "🎭",
                "severity": "emerging_critical",
                "visual_element": "Emerging threat burst"
            },
            {
                "date": "Oct 13",
                "event": "Phishing Coverage Collapse",
                "note": "Coverage dropped 70% (123 → 35 articles) = dangerous normalization",
                "icon": "⚠️",
                "severity": "warning",
                "visual_element": "Downward trend line"
            },
            {
                "date": "Oct 15",
                "event": "Multiple Incidents",
                "victims": "Noosa Council ($2.3M BEC), German Gov (DDoS), European Airports (system compromise)",
                "icon": "💥",
                "severity": "high",
                "visual_element": "Multiple simultaneous markers"
            }
        ],

        "visualization_type": "interactive_timeline",
        "visual_features": [
            "Horizontal timeline with vertical markers",
            "Icon-based event markers (different sizes for severity)",
            "Color-coded by threat type",
            "Hoverable for details",
            "Coverage intensity shown as bubble size",
            "Cost ranges as badge colors",
            "Connected events (e.g., JLR coverage spanning 3 weeks)"
        ]
    },

    # ============================================================================
    # SECTION 3: GEOGRAPHIC ATTACK MAP
    # ============================================================================
    "geographic_map": {
        "title": "Global Attack Distribution - Where Incidents Are Happening",
        "subtitle": "Coverage intensity by region with major incidents highlighted",

        "map_data": {
            "north_america": {
                "coverage_count": 2940,
                "percentage": 30.8,
                "trend": "stable",
                "major_incidents": [
                    {"victim": "AT&T", "location": "USA",
                        "cost": "$50M+", "icon": "📱"},
                    {"victim": "Multiple US Tech", "location": "USA",
                        "type": "Various", "icon": "💻"}
                ],
                "heat_level": "high",
                "color": "#EF4444"
            },
            "europe": {
                "coverage_count": 2012,
                "percentage": 21.1,
                "trend": "rising",
                "major_incidents": [
                    {"victim": "Jaguar Land Rover", "location": "UK",
                        "cost": "£50M+", "icon": "🚗"},
                    {"victim": "Brussels Airport", "location": "Belgium",
                        "cost": "€20M+", "icon": "🏢"},
                    {"victim": "German Government", "location": "Germany",
                        "type": "DDoS", "icon": "🏛️"}
                ],
                "heat_level": "critical",
                "color": "#DC2626"
            },
            "asia_pacific": {
                "coverage_count": 1447,
                "percentage": 15.2,
                "trend": "surging",
                "major_incidents": [
                    {"victim": "Asahi Group", "location": "Japan",
                        "cost": "¥2.3B", "icon": "🍺"},
                    {"victim": "Qantas", "location": "Australia",
                        "type": "Operations", "icon": "🛫"}
                ],
                "heat_level": "critical",
                "color": "#DC2626",
                "special_note": "Fastest growing region—ratio vs NA: 1:2 → 1:1.8"
            },
            "australia": {
                "coverage_count": 254,
                "percentage": 2.7,
                "trend": "rising",
                "major_incidents": [
                    {"victim": "Qantas", "location": "Sydney",
                        "impact": "Operations", "icon": "🛫"},
                    {"victim": "Noosa Council", "location": "Queensland",
                        "cost": "$2.3M", "icon": "🏛️"},
                    {"victim": "Electoral Commission", "location": "Canberra",
                        "type": "Deepfake warnings", "icon": "🗳️"}
                ],
                "heat_level": "high",
                "color": "#F97316",
                "special_note": "Highest per-capita coverage intensity globally"
            },
            "global_impact": {
                "coverage_count": 2230,
                "percentage": 23.4,
                "trend": "rising",
                "description": "Platform vulnerabilities, supply chain attacks, international threat actors",
                "major_incidents": [
                    {"victim": "Salesforce", "type": "Platform vuln", "icon": "☁️"},
                    {"victim": "Microsoft Azure",
                        "type": "Multiple incidents", "icon": "☁️"}
                ],
                "heat_level": "critical",
                "color": "#DC2626"
            }
        },

        "visualization_type": "world_map_with_pins",
        "visual_features": [
            "Heat map overlay (darker = more coverage)",
            "Pin markers for major incidents (sized by cost/impact)",
            "Animated trend arrows showing regional growth",
            "Hoverable regions showing stats",
            "Incident icons for quick threat type identification"
        ]
    },

    # ============================================================================
    # SECTION 4: COST IMPACT DASHBOARD
    # ============================================================================
    "cost_dashboard": {
        "title": "Financial Impact Analysis - Real Attack Costs",
        "subtitle": "Beyond ransom payments: the true cost of cyber incidents",

        "cost_breakdown_visual": {
            "example_incident": "Mid-Market Ransomware Attack",
            "total_cost": "$10M",

            "cost_components": [
                {
                    "category": "Ransom Payment",
                    "amount": "$500K",
                    "percentage": 5,
                    "color": "#DC2626",
                    "icon": "💰",
                    "note": "Often smallest cost component"
                },
                {
                    "category": "Recovery & Forensics",
                    "amount": "$2M",
                    "percentage": 20,
                    "color": "#EA580C",
                    "icon": "🔧",
                    "includes": ["Incident response", "Forensics investigation", "System restoration", "Data recovery"]
                },
                {
                    "category": "Operational Disruption",
                    "amount": "$3M",
                    "percentage": 30,
                    "color": "#F97316",
                    "icon": "⏸️",
                    "includes": ["Lost revenue during downtime", "Overtime for recovery", "Expedited vendor costs"]
                },
                {
                    "category": "Reputation & Customer Impact",
                    "amount": "$3M",
                    "percentage": 30,
                    "color": "#FB923C",
                    "icon": "📉",
                    "includes": ["Customer churn", "Brand damage", "Sales pipeline impact", "Customer compensation"]
                },
                {
                    "category": "Legal & Regulatory",
                    "amount": "$1M",
                    "percentage": 10,
                    "color": "#FDBA74",
                    "icon": "⚖️",
                    "includes": ["Regulatory fines", "Legal counsel", "Compliance remediation", "Lawsuits"]
                },
                {
                    "category": "Insurance Premium Increases",
                    "amount": "$500K",
                    "percentage": 5,
                    "color": "#FED7AA",
                    "icon": "📈",
                    "note": "50-200% premium increase for 3-5 years"
                }
            ],

            "visualization_type": "stacked_bar_or_sunburst",
            "key_insight": "Ransom is only 5% of total cost. Organizations focusing on payment decision are missing 95% of financial impact."
        },

        "real_incident_costs": {
            "title": "Recent Incidents - Estimated Financial Impact",

            "incidents": [
                {
                    "victim": "Jaguar Land Rover",
                    "total_cost": "£50M+",
                    "breakdown": {
                        "production_losses": "£35M",
                        "recovery_costs": "£8M",
                        "supply_chain_impacts": "£7M+",
                        "reputation": "Ongoing assessment"
                    },
                    "duration": "2 weeks primary disruption, months of delivery delays",
                    "visual": "Large bar chart with breakdown"
                },
                {
                    "victim": "Asahi Group",
                    "total_cost": "¥2.3B ($15M+)",
                    "breakdown": {
                        "immediate_response": "¥800M",
                        "operational_disruption": "¥1B",
                        "regulatory_legal": "¥500M+",
                        "long_term_impact": "Under assessment"
                    },
                    "duration": "Ongoing—earnings postponed",
                    "visual": "Large bar chart with breakdown"
                },
                {
                    "victim": "Brussels Airport",
                    "total_cost": "€20M+",
                    "breakdown": {
                        "airline_compensation": "€15M",
                        "operational_losses": "€3M",
                        "recovery_costs": "€2M"
                    },
                    "impact": "50,000+ passengers affected",
                    "visual": "Medium bar chart"
                },
                {
                    "victim": "Noosa Council",
                    "total_cost": "$2.3M",
                    "breakdown": {
                        "direct_fraud_loss": "$2.3M",
                        "investigation_costs": "$200K",
                        "process_remediation": "$100K"
                    },
                    "note": "BEC requires fewer recovery costs than ransomware, but direct loss is total",
                    "visual": "Small bar chart"
                }
            ],

            "visualization_type": "comparative_bar_chart",
            "visual_features": [
                "Sortable by total cost",
                "Color-coded by incident type",
                "Breakdown shows on hover",
                "Icons for incident type",
                "Duration timeline shown"
            ]
        },

        "cost_trends": {
            "title": "Cost Intelligence Trends",

            "insights": [
                {
                    "trend": "Ransom Payments Declining as % of Total Cost",
                    "data": "2020: 20% of total | 2023: 10% | 2025: <5%",
                    "why": "Recovery infrastructure improved, but operational disruption and reputation costs exploding",
                    "visual": "Line chart showing declining percentage",
                    "icon": "📉"
                },
                {
                    "trend": "Operational Disruption Costs Rising",
                    "data": "Now 30-40% of total incident cost (was 15-20% in 2020)",
                    "why": "Digital dependence increased, operational tempo accelerated, downtime tolerance decreased",
                    "visual": "Rising line chart",
                    "icon": "📈"
                },
                {
                    "trend": "Cyber Insurance Premiums Spiking",
                    "data": "50-200% increases post-incident, coverage limits decreasing",
                    "why": "Insurance market tightening as claims skyrocket. Healthcare sector facing crisis.",
                    "visual": "Step chart showing premium jumps",
                    "icon": "🚨"
                },
                {
                    "trend": "Regulatory Penalties Increasing",
                    "data": "GDPR fines up 145% year-over-year, SEC penalties up 89%",
                    "why": "Regulators using cybersecurity to demonstrate authority",
                    "visual": "Bar chart comparing years",
                    "icon": "⚖️"
                }
            ]
        }
    },

    # ============================================================================
    # SECTION 5: THREAT ACTOR INTELLIGENCE CARDS
    # ============================================================================
    "threat_actor_cards": {
        "title": "Active Threat Actors - Who's Operating and How",
        "subtitle": "Intelligence on the groups behind major attacks",

        "actor_profiles": [
            {
                "name": "Scattered Spider",
                "rank": "#1 Most Covered",
                "articles": 251,
                "days_active": 29,
                "coverage_trend": "sustained",
                "sophistication": "High",
                "primary_method": "Social Engineering",
                "recent_victim": "Jaguar Land Rover",
                "estimated_damage": "£50M+",
                "signature": "High-visibility targeting, sustained operational tempo, media-savvy disclosure timing",
                "threat_level": "🔴 Critical",
                "visual_elements": {
                    "activity_chart": "29-day timeline showing sustained coverage",
                    "target_map": "Geographic distribution of victims",
                    "method_breakdown": "Pie chart of tactics"
                },
                "icon": "🕷️",
                "color": "#DC2626"
            },
            {
                "name": "Qilin",
                "rank": "#2 Financial Impact",
                "articles": 61,
                "days_active": 21,
                "coverage_trend": "increasing",
                "sophistication": "High",
                "primary_method": "Ransomware (RaaS)",
                "recent_victim": "Asahi Group Holdings",
                "estimated_damage": "¥2.3B ($15M+)",
                "signature": "Professional leak sites, countdown timers, targeting non-traditional sectors (F&B)",
                "threat_level": "🔴 Critical",
                "visual_elements": {
                    "ransom_timeline": "Pressure campaign visualization",
                    "sector_targeting": "Industry distribution"
                },
                "icon": "🐉",
                "color": "#DC2626"
            },
            {
                "name": "Scattered Lapsus$ Hunters",
                "rank": "#3 Coverage Velocity",
                "articles": 179,
                "days_active": 27,
                "coverage_trend": "increasing",
                "sophistication": "High",
                "primary_method": "Credential Theft",
                "targets": "Technology sector, SaaS platforms",
                "signature": "Brand leveraging (referencing Lapsus$), media-friendly naming",
                "threat_level": "🟠 High",
                "icon": "🎯",
                "color": "#EA580C"
            },
            {
                "name": "Kimsuky (APT)",
                "rank": "#4 Nation-State",
                "articles": 59,
                "days_active": 14,
                "coverage_trend": "emerging",
                "sophistication": "High",
                "primary_method": "Spear Phishing / Long-term infiltration",
                "attribution": "North Korea (nation-state)",
                "targets": "Government, think tanks, research institutions",
                "signature": "Patient reconnaissance, intelligence gathering objectives",
                "threat_level": "🔴 Critical (geopolitical)",
                "icon": "🎖️",
                "color": "#991B1B"
            },
            {
                "name": "ShinyHunters",
                "rank": "#5 Commodity Breaches",
                "articles": 89,
                "days_active": 23,
                "coverage_trend": "stable",
                "sophistication": "Medium",
                "primary_method": "Database exploitation, misconfigurations",
                "targets": "E-commerce, SaaS platforms",
                "signature": "Volume tactics, data broker operations, exposed database exploitation",
                "threat_level": "🟡 Medium",
                "icon": "💎",
                "color": "#F59E0B"
            }
        ],

        "visualization_type": "interactive_cards",
        "visual_features": [
            "Card layout with actor photos/logos",
            "Activity sparklines showing coverage over time",
            "Threat level badges (color-coded)",
            "Hover for detailed stats",
            "Click to expand full profile",
            "Filterable by sophistication, method, active status"
        ]
    },

    # ============================================================================
    # SECTION 6: SECTOR VULNERABILITY MATRIX
    # ============================================================================
    "sector_matrix": {
        "title": "Industry Vulnerability Assessment",
        "subtitle": "Which sectors are under fire and why",

        "matrix_data": [
            {
                "sector": "Transportation & Aviation",
                "vulnerability_score": 9.1,
                "coverage_growth": "+31.5%",
                "incident_count": 238,
                "why_targeted": "Visible consumer disruption creates media pressure = operational leverage for attackers",
                "recent_incidents": ["Brussels Airport", "Qantas", "Heathrow"],
                "avg_cost": "€5M-€50M per incident",
                "risk_factors": ["Operational visibility", "Consumer impact", "Safety concerns", "Just-in-time operations"],
                "defensive_maturity": "Low-Medium",
                "color": "#DC2626",
                "icon": "✈️"
            },
            {
                "sector": "Manufacturing",
                "vulnerability_score": 8.9,
                "coverage_growth": "+23.1%",
                "incident_count": 618,
                "why_targeted": "Just-in-time = zero buffer capacity. Single failure cascades to multi-facility shutdown",
                "recent_incidents": ["Jaguar Land Rover"],
                "avg_cost": "£20M-£100M per incident",
                "risk_factors": ["OT/IT convergence", "Supply chain complexity", "Legacy industrial systems", "Production dependencies"],
                "defensive_maturity": "Low",
                "color": "#DC2626",
                "icon": "🏭"
            },
            {
                "sector": "Technology & SaaS",
                "vulnerability_score": 8.2,
                "coverage_growth": "+8.2%",
                "incident_count": 4015,
                "why_targeted": "Platform attacks = multiplier effect. One vulnerability affects thousands simultaneously",
                "recent_incidents": ["Salesforce", "Microsoft", "Discord"],
                "avg_cost": "Multiplier—varies by customer base",
                "risk_factors": ["Platform concentration", "Supply chain role", "High-value targets", "Complexity"],
                "defensive_maturity": "Medium-High",
                "color": "#EA580C",
                "icon": "💻"
            },
            {
                "sector": "Financial Services",
                "vulnerability_score": 7.8,
                "coverage_growth": "+5.3%",
                "incident_count": 2051,
                "why_targeted": "High-value data, regulatory attention, established attack patterns",
                "recent_incidents": ["AT&T (payment data)", "Multiple banking incidents"],
                "avg_cost": "$5M-$50M (regulatory penalties significant)",
                "risk_factors": ["Regulatory exposure", "High-value data", "Complex infrastructure", "Legacy systems"],
                "defensive_maturity": "High",
                "color": "#F97316",
                "icon": "💰"
            },
            {
                "sector": "Government",
                "vulnerability_score": 8.5,
                "coverage_growth": "+12.7%",
                "incident_count": 1358,
                "why_targeted": "Geopolitical objectives, election interference, espionage",
                "recent_incidents": ["German Government", "Australian Electoral Commission (warnings)"],
                "avg_cost": "Difficult to quantify—political impact primary concern",
                "risk_factors": ["Nation-state targeting", "Political sensitivity", "Budget constraints", "Legacy systems"],
                "defensive_maturity": "Medium",
                "color": "#EF4444",
                "icon": "🏛️"
            },
            {
                "sector": "Healthcare",
                "vulnerability_score": 7.5,
                "coverage_growth": "+3.2%",
                "incident_count": 661,
                "why_targeted": "Ransomware groups know healthcare pays due to patient care pressure",
                "recent_incidents": ["Multiple (normalized—minimal individual coverage)"],
                "avg_cost": "$5M-$20M per incident",
                "risk_factors": ["Life-safety pressure", "Legacy medical devices", "Ransomware normalization", "Limited budgets"],
                "defensive_maturity": "Low-Medium",
                "color": "#F59E0B",
                "icon": "🏥",
                "special_note": "Dangerous normalization—frequent attacks getting minimal coverage"
            }
        ],

        "visualization_type": "matrix_grid",
        "visual_features": [
            "Grid layout with color-coded vulnerability scores",
            "Growth arrows (size indicates velocity)",
            "Hover shows recent incidents and costs",
            "Sortable by vulnerability score, growth, incident count",
            "Defensive maturity shown as progress bar",
            "Icons for quick sector identification"
        ]
    },

    # ============================================================================
    # SECTION 7: EMERGING THREAT RADAR
    # ============================================================================
    "emerging_threat_radar": {
        "title": "Emerging Threat Radar - What's Coming Next",
        "subtitle": "Early signals of threats gaining momentum",

        "radar_quadrants": {
            "critical_emerging": [
                {
                    "threat": "Deepfake Authentication Attacks",
                    "current_stage": "Breakthrough moment—mainstream coverage",
                    "growth_rate": "+47% WoW",
                    "time_to_mainstream": "Already arrived—90 days to market saturation",
                    "indicators": [
                        "Australian Electoral Commission warnings = political legitimization",
                        "Coverage jumped from tech press to mainstream news",
                        "Real business fraud cases documented"
                    ],
                    "icon": "🎭",
                    "urgency": "🔴 Act Now",
                    "position": {"urgency": 95, "maturity": 60}
                }
            ],
            "high_emerging": [
                {
                    "threat": "Manufacturing/OT Targeting",
                    "current_stage": "Rapid growth but under-analyzed",
                    "growth_rate": "+23.1%",
                    "time_to_mainstream": "6-12 months",
                    "indicators": [
                        "JLR incident revealed just-in-time vulnerability",
                        "Coverage still mostly trade press",
                        "Supply chain implications becoming visible"
                    ],
                    "icon": "🏭",
                    "urgency": "🟠 Prepare Now",
                    "position": {"urgency": 75, "maturity": 35}
                },
                {
                    "threat": "Platform Concentration Risk",
                    "current_stage": "Emerging recognition",
                    "growth_rate": "+15%",
                    "time_to_mainstream": "12-18 months",
                    "indicators": [
                        "Salesforce vulnerability affected thousands simultaneously",
                        "SaaS concentration creating systemic risk",
                        "Supply chain security expanding to platform dependencies"
                    ],
                    "icon": "☁️",
                    "urgency": "🟡 Monitor Closely",
                    "position": {"urgency": 70, "maturity": 40}
                }
            ],
            "medium_emerging": [
                {
                    "threat": "AI-Enhanced Social Engineering",
                    "current_stage": "Early adoption by threat actors",
                    "growth_rate": "+18%",
                    "time_to_mainstream": "18-24 months",
                    "indicators": [
                        "Phishing coverage declining but threat evolving",
                        "AI personalization enabling scale",
                        "Multi-channel coordination increasing"
                    ],
                    "icon": "🤖",
                    "urgency": "🟡 Monitor",
                    "position": {"urgency": 60, "maturity": 30}
                },
                {
                    "threat": "Nation-State Tactics Going Commercial",
                    "current_stage": "Early signals in attribution coverage",
                    "growth_rate": "+12%",
                    "time_to_mainstream": "24+ months",
                    "indicators": [
                        "Criminal groups adopting APT techniques",
                        "Patient reconnaissance becoming common",
                        "Living-off-the-land tactics in ransomware operations"
                    ],
                    "icon": "🎖️",
                    "urgency": "🟢 Awareness",
                    "position": {"urgency": 50, "maturity": 25}
                }
            ],
            "watch_list": [
                {
                    "threat": "Quantum Computing Threats",
                    "current_stage": "Theoretical/preparation phase",
                    "growth_rate": "+5%",
                    "time_to_mainstream": "36+ months",
                    "indicators": [
                        "Minimal current coverage",
                        "Cryptography community preparing",
                        "Long lead time for organizational preparation"
                    ],
                    "icon": "⚛️",
                    "urgency": "🔵 Long-term Watch",
                    "position": {"urgency": 30, "maturity": 10}
                }
            ]
        },

        "visualization_type": "radar_chart",
        "visual_features": [
            "Radar/bubble chart with urgency (x-axis) vs maturity (y-axis)",
            "Bubble size = growth rate",
            "Color coding by urgency level",
            "Animated movement showing threat velocity",
            "Quadrants: Critical/High/Medium/Watch",
            "Click bubbles for detailed breakdown"
        ]
    },

    # ============================================================================
    # SECTION 8: KEY INCIDENTS SHOWCASE
    # ============================================================================
    "incidents_showcase": {
        "title": "Featured Incidents - Deep Dive Analysis",
        "subtitle": "Detailed breakdowns of the month's most significant attacks",

        "featured_incidents": [
            {
                "incident_id": "JLR-2025-10",
                "title": "Jaguar Land Rover Supply Chain Breach",
                "tagline": "How One Compromised Portal Shut Down £50M+ of Production",

                "hero_stats": {
                    "total_cost": "£50M+",
                    "duration": "2 weeks active disruption",
                    "coverage": "420 articles over 3 weeks",
                    "impact": "3 facilities, months of delivery delays"
                },

                "timeline": [
                    {"date": "Sep 18", "event": "Initial compromise detected", "icon": "🔍"},
                    {"date": "Sep 19",
                        "event": "Production halted at UK facilities", "icon": "⏸️"},
                    {"date": "Sep 20", "event": "Media coverage begins", "icon": "📰"},
                    {"date": "Sep 22",
                        "event": "Scattered Spider attribution confirmed", "icon": "🕷️"},
                    {"date": "Sep 25", "event": "Supply chain impacts visible", "icon": "🔗"},
                    {"date": "Oct 2", "event": "Partial production resumed", "icon": "▶️"},
                    {"date": "Oct 8", "event": "Full operations restored", "icon": "✅"},
                    {"date": "Ongoing", "event": "Delivery delays continue", "icon": "📦"}
                ],

                "attack_chain": [
                    {"step": 1, "phase": "Initial Access",
                        "detail": "Social engineering compromise of supplier portal credentials", "icon": "🎣"},
                    {"step": 2, "phase": "Lateral Movement",
                        "detail": "Pivot from supplier network to JLR production systems", "icon": "➡️"},
                    {"step": 3, "phase": "Persistence",
                        "detail": "Establish foothold in manufacturing control systems", "icon": "🔒"},
                    {"step": 4, "phase": "Impact",
                        "detail": "Disrupt production scheduling and supply chain coordination", "icon": "💥"}
                ],

                "business_impact": {
                    "production_losses": "£35M (estimated lost production value)",
                    "recovery_costs": "£8M (incident response, system restoration)",
                    "supply_chain": "£7M+ (supplier impacts, expedited shipping)",
                    "reputation": "Ongoing—delivery delays affecting customer satisfaction",
                    "regulatory": "Under investigation"
                },

                "media_coverage_arc": {
                    "description": "Self-sustaining news cycle over 3 weeks",
                    "phases": [
                        {"week": 1, "theme": "Breaking news—production halted",
                            "article_count": 180},
                        {"week": 2, "theme": "Attribution, supply chain impacts",
                            "article_count": 140},
                        {"week": 3, "theme": "Recovery timeline, industry implications",
                            "article_count": 100}
                    ]
                },

                "key_lessons": [
                    "Just-in-time manufacturing has zero buffer capacity—digital failure = immediate physical shutdown",
                    "Supplier portal security as critical as internal systems—supply chain is attack surface",
                    "Visible operational disruption creates media frenzy = board pressure = crisis management challenge",
                    "Automotive industry faces systemic OT/IT convergence risk"
                ],

                "article_examples": [
                    {"outlet": "Financial Times",
                        "headline": "JLR halts production at UK plants following cyberattack", "date": "Sep 19"},
                    {"outlet": "Reuters", "headline": "Scattered Spider's automotive targeting signals new threat actor strategy", "date": "Sep 22"},
                    {"outlet": "BBC", "headline": "Jaguar customers face months-long delivery delays after breach", "date": "Sep 25"},
                    {"outlet": "Automotive News",
                        "headline": "JLR breach exposes automotive cybersecurity vulnerabilities", "date": "Sep 28"}
                ],

                "visual_elements": {
                    "cost_breakdown_chart": "Stacked bar showing £50M+ distribution",
                    "timeline_visualization": "Interactive event timeline",
                    "coverage_arc_graph": "Line chart showing 3-week coverage pattern",
                    "attack_chain_diagram": "Flow diagram of compromise stages",
                    "supply_chain_map": "Network diagram showing cascade effects"
                }
            },
            {
                "incident_id": "ASAHI-2025-10",
                "title": "Asahi Group Ransomware Attack",
                "tagline": "Japanese Corporate Transparency Breakthrough—¥2.3B Crisis",

                "hero_stats": {
                    "total_cost": "¥2.3B ($15M+)",
                    "files_compromised": "9,300+",
                    "coverage": "95 articles across APAC and global press",
                    "cultural_significance": "First major Japanese company with full public disclosure"
                },

                "timeline": [
                    {"date": "Oct 8",
                        "event": "Ransomware deployment detected", "icon": "🚨"},
                    {"date": "Oct 9", "event": "Operations disrupted, data exfiltration confirmed", "icon": "📤"},
                    {"date": "Oct 10", "event": "Public disclosure—unprecedented transparency", "icon": "📢"},
                    {"date": "Oct 11", "event": "Qilin group claims responsibility, leak site activated", "icon": "🐉"},
                    {"date": "Oct 12", "event": "Earnings release postponed", "icon": "📊"},
                    {"date": "Oct 14", "event": "Recovery operations ongoing", "icon": "🔧"}
                ],

                "attack_chain": [
                    {"step": 1, "phase": "Initial Access",
                        "detail": "Entry vector undisclosed (likely phishing or vulnerability)", "icon": "🔓"},
                    {"step": 2, "phase": "Reconnaissance",
                        "detail": "Network mapping, data identification", "icon": "🔍"},
                    {"step": 3, "phase": "Data Exfiltration",
                        "detail": "9,300+ files stolen before encryption", "icon": "📤"},
                    {"step": 4, "phase": "Ransomware Deployment",
                        "detail": "Qilin ransomware encrypted systems", "icon": "🔒"},
                    {"step": 5, "phase": "Extortion",
                        "detail": "Leak site with countdown timer pressuring payment", "icon": "⏰"}
                ],

                "business_impact": {
                    "immediate_response": "¥800M (incident response, forensics, initial recovery)",
                    "operational_disruption": "¥1B (production impact, business continuity)",
                    "regulatory_legal": "¥500M+ (investigations, potential penalties, legal costs)",
                    "earnings_impact": "Postponed—unprecedented for Japanese public company",
                    "reputation": "Cultural shift—transparency may establish new norms"
                },

                "cultural_significance": {
                    "context": "Japanese corporations historically minimize public discussion of cyber incidents due to reputation concerns",
                    "breakthrough": "Asahi provided detailed public updates, postponed earnings, acknowledged data compromise",
                    "why_different": "Qilin's leak site pressure tactics + Japanese data protection law requirements = forced transparency",
                    "implications": "May establish new disclosure expectations across Asian markets",
                    "market_signal": "Asian corporate cyber disclosure culture evolving rapidly"
                },

                "key_lessons": [
                    "Double-extortion ransomware (data theft + encryption) forces disclosure even in reticent cultures",
                    "Earnings calendar pressure accelerates disclosure decisions—can't postpone indefinitely",
                    "Transparent response generated more positive coverage than attempted cover-up would have",
                    "Food & beverage industry—non-traditional target showing ransomware group sector diversification"
                ],

                "article_examples": [
                    {"outlet": "Nikkei Asia", "headline": "Asahi Group postpones earnings announcement following ransomware attack", "date": "Oct 12"},
                    {"outlet": "Japan Times",
                        "headline": "Personal information possibly leaked in cyberattack on Asahi group", "date": "Oct 10"},
                    {"outlet": "Bloomberg", "headline": "Japanese beverage giant's cyber woes signal cultural shift in disclosure", "date": "Oct 13"},
                    {"outlet": "Reuters", "headline": "Qilin ransomware group claims responsibility for Asahi breach", "date": "Oct 11"}
                ],

                "visual_elements": {
                    "cost_breakdown_yen": "¥2.3B distribution pie chart",
                    "cultural_comparison": "Chart comparing disclosure timelines: Japanese vs Western companies",
                    "qilin_leak_site": "Screenshot/mockup of leak site pressure tactics",
                    "coverage_geography": "Map showing APAC vs global coverage distribution"
                }
            },
            {
                "incident_id": "BRUSSELS-2025-10",
                "title": "Brussels Airport Critical Infrastructure Outage",
                "tagline": "50,000 Passengers Stranded—€20M+ Impact from Ambiguous Incident",

                "hero_stats": {
                    "total_cost": "€20M+",
                    "passengers_affected": "50,000+",
                    "duration": "5 days of disruption",
                    "coverage": "116 articles despite unclear attribution"
                },

                "timeline": [
                    {"date": "Oct 5",
                        "event": "Check-in systems fail unexpectedly", "icon": "❌"},
                    {"date": "Oct 5",
                        "event": "Manual check-in processes implemented", "icon": "📝"},
                    {"date": "Oct 6", "event": "Media coverage begins—'possible cyberattack'", "icon": "📰"},
                    {"date": "Oct 7", "event": "Investigation ongoing, technical details limited", "icon": "🔍"},
                    {"date": "Oct 9", "event": "Partial systems restored", "icon": "🔄"},
                    {"date": "Oct 10", "event": "Full operations resumed", "icon": "✅"}
                ],

                "key_mystery": {
                    "question": "Was this a cyberattack, system failure, or something else?",
                    "status": "Never definitively confirmed",
                    "coverage_impact": "Generated 116 articles despite ambiguity—suspicion alone newsworthy",
                    "lesson": "'Cyber' has become default explanation for any unexpected technical failure in critical infrastructure"
                },

                "business_impact": {
                    "airline_compensation": "€15M (EU passenger rights regulations)",
                    "airport_operational_losses": "€3M (lost revenue during disruption)",
                    "recovery_investigation": "€2M (technical investigation, system restoration)",
                    "reputation": "Political pressure on aviation cybersecurity preparedness"
                },

                "why_this_matters": {
                    "point_1": "Critical infrastructure + consumer disruption = guaranteed sustained coverage",
                    "point_2": "Attribution uncertainty doesn't reduce coverage—speculation fills information vacuum",
                    "point_3": "Visible chaos (stranded passengers) creates human-interest stories that data breaches can't",
                    "point_4": "Political context (EU infrastructure protection debates) amplified coverage"
                },

                "key_lessons": [
                    "Crisis communications plans must account for ambiguous incidents—can't wait for attribution",
                    "Consumer-facing disruption generates coverage disproportionate to technical severity",
                    "Critical infrastructure incidents treated as public safety issues, not just business problems",
                    "Photography matters—visual chaos drives sustained media attention"
                ],

                "article_examples": [
                    {"outlet": "The Guardian",
                        "headline": "Brussels Airport chaos as cyber incident forces manual check-ins", "date": "Oct 5"},
                    {"outlet": "Le Monde",
                        "headline": "Cyberattaque possible sur l'aéroport de Bruxelles", "date": "Oct 6"},
                    {"outlet": "Financial Times",
                        "headline": "Aviation industry faces questions over cybersecurity preparedness", "date": "Oct 8"},
                    {"outlet": "Politico EU",
                        "headline": "Brussels airport outage raises infrastructure security concerns", "date": "Oct 9"}
                ],

                "visual_elements": {
                    "passenger_impact_infographic": "50,000+ affected visualization",
                    "cost_breakdown_euros": "€20M+ distribution",
                    "timeline_with_photos": "Event timeline with passenger chaos imagery",
                    "coverage_intensity_map": "European press coverage distribution"
                }
            }
        ],

        "visualization_type": "expandable_cards",
        "visual_features": [
            "Card grid for incident overview",
            "Click to expand full detailed breakdown",
            "Interactive timelines with hover details",
            "Cost breakdown charts",
            "Attack chain flow diagrams",
            "Article quote callouts with outlet logos",
            "Photo galleries where available",
            "Lessons learned highlighted sections"
        ]
    },

    # ============================================================================
    # SECTION 9: LIVE INTELLIGENCE FEED
    # ============================================================================
    "intelligence_feed": {
        "title": "Latest Intelligence - Real-Time Coverage Signals",
        "subtitle": "Breaking patterns and emerging stories from the last 48 hours",

        "feed_items": [
            {
                "timestamp": "2 hours ago",
                "type": "coverage_spike",
                "title": "Coverage Spike: Zero-Day Vulnerability",
                "description": "Oracle zero-day exploitation mentioned in 43 articles in past 6 hours—unusual velocity suggests coordinated disclosure or active exploitation",
                "severity": "high",
                "icon": "🔓",
                "action": "Monitor for expansion into broader coverage"
            },
            {
                "timestamp": "5 hours ago",
                "type": "new_incident",
                "title": "New Incident: UK Healthcare Ransomware",
                "description": "NHS trust reportedly hit by ransomware, patient care systems affected. Only 3 articles so far but healthcare + patient impact suggests coverage will grow",
                "severity": "medium",
                "icon": "🏥",
                "action": "Watch for coverage escalation over next 24h"
            },
            {
                "timestamp": "12 hours ago",
                "type": "threat_actor",
                "title": "Threat Actor: New Group Claims Major Breach",
                "description": "Previously unknown group 'Phantom Syndicate' claiming responsibility for Fortune 500 data breach. Attribution uncertain but media picking up story",
                "severity": "medium",
                "icon": "👻",
                "action": "Monitor attribution confirmation"
            },
            {
                "timestamp": "18 hours ago",
                "type": "regulatory",
                "title": "Regulatory: EU Announces Critical Infrastructure Directive",
                "description": "European Commission announcing new cybersecurity requirements for critical infrastructure operators. 27 articles covering policy implications",
                "severity": "info",
                "icon": "📜",
                "action": "Policy analysis—affects transportation, energy, utilities"
            },
            {
                "timestamp": "24 hours ago",
                "type": "coverage_trend",
                "title": "Trend Alert: Deepfake Coverage Sustaining",
                "description": "Deepfake-related articles maintaining 40+ per day for 5 consecutive days. Narrative has achieved sustained mainstream presence",
                "severity": "info",
                "icon": "🎭",
                "action": "Thought leadership window closing—market saturating"
            }
        ],

        "visualization_type": "timeline_feed",
        "visual_features": [
            "Reverse chronological feed",
            "Color-coded by severity (red/orange/yellow/blue)",
            "Icons for quick categorization",
            "Real-time updates (in actual version)",
            "Filterable by type, severity",
            "Click for full article list"
        ]
    },

    # ============================================================================
    # SECTION 10: COVERAGE QUALITY INDICATORS
    # ============================================================================
    "coverage_quality": {
        "title": "Coverage Quality Assessment",
        "subtitle": "Understanding the depth and sophistication of cybersecurity journalism",

        "quality_metrics": [
            {
                "metric": "Technical Depth Score",
                "current_value": 6.2,
                "scale": "1-10 (10 = highly technical)",
                "trend": "Declining",
                "interpretation": "Coverage becoming more business-focused, less technically detailed. Good for executive audience, bad for practitioner implementation guidance",
                "visual": "Gauge chart showing 6.2/10"
            },
            {
                "metric": "Attribution Confidence",
                "current_value": "Medium",
                "details": "57% of articles include specific threat actor attribution, up from 42% last year",
                "trend": "Improving",
                "interpretation": "Journalism sophistication increasing—more confident in naming groups, tracking campaigns vs isolated incidents",
                "visual": "Progress bar at 57%"
            },
            {
                "metric": "Business Impact Framing",
                "current_value": "High",
                "details": "73% of major incident coverage emphasizes operational/financial impact over technical details",
                "trend": "Increasing",
                "interpretation": "Cybersecurity achieving 'legitimate business journalism' status. Board-level framing now dominant",
                "visual": "Progress bar at 73%"
            },
            {
                "metric": "Source Diversity",
                "current_value": "Medium-High",
                "details": "Average article cites 2.8 sources (vendor, analyst, victim organization, law enforcement)",
                "trend": "Stable",
                "interpretation": "Solid multi-source verification, but vendor voices still dominate (42% of quoted sources)",
                "visual": "Source breakdown pie chart"
            },
            {
                "metric": "Actionable Guidance Ratio",
                "current_value": "Low",
                "details": "Only 18% of articles include specific defensive recommendations",
                "trend": "Stable",
                "interpretation": "Coverage heavy on 'what happened,' light on 'what to do about it.' Thought leadership opportunity",
                "visual": "Bar chart comparing incident coverage vs guidance"
            }
        ],

        "media_sophistication_examples": {
            "high_quality": [
                {
                    "outlet": "Financial Times",
                    "article": "JLR breach analysis",
                    "why_good": "Multi-source, business impact emphasis, supply chain implications, board accountability framing",
                    "quote": "'The attack exposed fundamental vulnerabilities in automotive just-in-time manufacturing'"
                },
                {
                    "outlet": "Reuters",
                    "article": "Scattered Spider attribution",
                    "why_good": "Threat actor profiling, tactical analysis, strategic implications, multiple security researcher sources",
                    "quote": "'Social engineering sophistication suggests evolution beyond traditional ransomware operations'"
                }
            ],
            "low_quality": [
                {
                    "example": "Generic 'hackers strike again' headline",
                    "why_poor": "No attribution, technical detail, or business context. Pure sensationalism",
                    "prevalence": "Still ~25% of coverage in general interest media"
                }
            ]
        }
    }
}

# ============================================================================
# VISUAL DESIGN SYSTEM
# ============================================================================

visual_design_system = {
    "color_palette": {
        "severity_colors": {
            "critical": "#DC2626",      # Red
            "high": "#EA580C",          # Orange-Red
            "medium": "#F59E0B",        # Amber
            "low": "#FCD34D",           # Yellow
            "info": "#3B82F6",          # Blue
            "positive": "#10B981"       # Green
        },
        "trend_colors": {
            "surging": "#DC2626",       # Red (alarming)
            "rising": "#F97316",        # Orange
            "stable": "#6B7280",        # Gray
            "declining": "#3B82F6"      # Blue
        },
        "sector_colors": {
            "transportation": "#DC2626",
            "manufacturing": "#EA580C",
            "technology": "#F59E0B",
            "financial": "#F97316",
            "government": "#EF4444",
            "healthcare": "#F59E0B"
        }
    },

    "typography": {
        "headers": {
            "main_title": "2.5rem, bold, #1E3A8A",
            "section_title": "1.75rem, semibold, #1F2937",
            "card_title": "1.25rem, semibold, #374151"
        },
        "body": {
            "primary": "1rem, regular, #4B5563",
            "secondary": "0.875rem, regular, #6B7280",
            "caption": "0.75rem, regular, #9CA3AF"
        }
    },

    "icons_and_emojis": {
        "threat_types": {
            "ransomware": "🔒",
            "supply_chain": "🔗",
            "deepfake": "🎭",
            "infrastructure": "⚡",
            "platform": "☁️",
            "bec": "🎣",
            "data_breach": "📁"
        },
        "severity": {
            "critical": "🔴",
            "high": "🟠",
            "medium": "🟡",
            "low": "🟢"
        },
        "trends": {
            "up": "📈",
            "down": "📉",
            "stable": "➡️"
        }
    },

    "layout_principles": [
        "Visual hierarchy: Most important incidents = largest visual elements",
        "Color coding: Consistent severity/threat type colors throughout",
        "Interactive elements: Hover for details, click for expansion",
        "Scannable: Icons, colors, and size variations enable quick pattern recognition",
        "Data-ink ratio: Maximize information, minimize decoration",
        "White space: Breathing room between dense information sections",
        "Progressive disclosure: Overview → details on interaction"
    ]
}
