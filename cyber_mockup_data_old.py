# mock_data.py
# Comprehensive static data for cybersecurity trends dashboard mockup
# Focus: Rich narrative insights with compelling details and expert commentary

from datetime import datetime, timedelta

# ============================================================================
# DAILY METRICS DATA
# ============================================================================

daily_articles = [
    {"date": "2025-09-15", "article_count": 368, "unique_outlets": 142},
    {"date": "2025-09-16", "article_count": 353, "unique_outlets": 138},
    {"date": "2025-09-17", "article_count": 386, "unique_outlets": 151},
    {"date": "2025-09-18", "article_count": 320, "unique_outlets": 129},
    {"date": "2025-09-19", "article_count": 342, "unique_outlets": 145},
    {"date": "2025-09-20", "article_count": 259, "unique_outlets": 118},
    {"date": "2025-09-21", "article_count": 232, "unique_outlets": 102},
    {"date": "2025-09-22", "article_count": 466, "unique_outlets": 178},
    {"date": "2025-09-23", "article_count": 447, "unique_outlets": 169},
    {"date": "2025-09-24", "article_count": 388, "unique_outlets": 156},
    {"date": "2025-09-25", "article_count": 378, "unique_outlets": 148},
    {"date": "2025-09-26", "article_count": 440, "unique_outlets": 172},
    {"date": "2025-09-27", "article_count": 204, "unique_outlets": 95},
    {"date": "2025-09-28", "article_count": 192, "unique_outlets": 89},
    {"date": "2025-09-29", "article_count": 384, "unique_outlets": 152},
    {"date": "2025-09-30", "article_count": 351, "unique_outlets": 141},
    {"date": "2025-10-01", "article_count": 54, "unique_outlets": 48},
    {"date": "2025-10-02", "article_count": 299, "unique_outlets": 127},
    {"date": "2025-10-03", "article_count": 420, "unique_outlets": 165},
    {"date": "2025-10-04", "article_count": 174, "unique_outlets": 86},
    {"date": "2025-10-05", "article_count": 173, "unique_outlets": 84},
    {"date": "2025-10-06", "article_count": 386, "unique_outlets": 153},
    {"date": "2025-10-07", "article_count": 36, "unique_outlets": 34},
    {"date": "2025-10-08", "article_count": 339, "unique_outlets": 136},
    {"date": "2025-10-09", "article_count": 373, "unique_outlets": 147},
    {"date": "2025-10-10", "article_count": 409, "unique_outlets": 162},
    {"date": "2025-10-11", "article_count": 185, "unique_outlets": 91},
    {"date": "2025-10-12", "article_count": 208, "unique_outlets": 98},
    {"date": "2025-10-13", "article_count": 349, "unique_outlets": 139},
    {"date": "2025-10-14", "article_count": 60, "unique_outlets": 52},
]

# ============================================================================
# KEYWORD/TOPIC TRENDS DATA
# ============================================================================

keyword_trends = [
    {
        "keyword": "Cyberattack",
        "current_count": 1113,
        "previous_count": 986,
        "change_percent": 12.9,
        "trend": "rising",
        "sentiment": "negative",
        "days_active": 30,
        "peak_date": "2025-09-26",
        "narrative": "The term 'cyberattack' has become the media's preferred catch-all, appearing in everything from nation-state operations to script-kiddie exploits. Its 13% growth reflects journalism's struggle to differentiate between APT campaigns and opportunistic scanning—a linguistic laziness that obscures actual threat sophistication.",
        "expert_take": "When journalists default to 'cyberattack' instead of specific terminology (breach, compromise, exploitation), it signals either lack of technical detail in sources or deliberate oversimplification for general audiences. The term's growth correlates with mainstream media entering cybersecurity coverage—breadth over depth."
    },
    {
        "keyword": "Ransomware",
        "current_count": 761,
        "previous_count": 698,
        "change_percent": 9.0,
        "trend": "rising",
        "sentiment": "negative",
        "days_active": 30,
        "peak_date": "2025-09-22",
        "narrative": "Ransomware coverage has matured from sensational 'hackers demand millions' headlines to nuanced business continuity analysis. The 9% growth masks a significant shift: media now emphasizes operational disruption over ransom payments, reflecting evolved understanding of true business impact.",
        "expert_take": "Coverage peaked Sept 22 around the Qilin-Asahi incident—notable because Japanese media typically under-reports cyberattacks due to corporate reputation concerns. That this broke through suggests ransomware has achieved 'undeniable business crisis' status even in disclosure-averse cultures."
    },
    {
        "keyword": "Phishing",
        "current_count": 669,
        "previous_count": 712,
        "change_percent": -6.0,
        "trend": "declining",
        "sentiment": "negative",
        "days_active": 30,
        "peak_date": "2025-09-01",
        "narrative": "The 6% decline in phishing coverage is deceptive—the threat hasn't diminished, but media has grown bored with 'generic phishing campaign' stories. What remains are sophisticated cases: AI-generated phishing, voice phishing (vishing) with deepfake audio, and targeted spear-phishing against executives. The mundane has become background noise.",
        "expert_take": "This is dangerous normalization. Phishing generates 80%+ of initial access vectors, yet declining coverage creates organizational complacency. The real story: phishing evolved into 'social engineering 2.0' but lost its media brand. When a threat becomes too common to report, security budgets start looking at it as 'solved problem.'"
    },
    {
        "keyword": "Malware",
        "current_count": 580,
        "previous_count": 623,
        "change_percent": -6.9,
        "trend": "declining",
        "sentiment": "negative",
        "days_active": 30,
        "peak_date": "2025-09-01",
        "narrative": "Generic 'malware' coverage is dying because the category is too broad to be meaningful. Modern journalism demands specificity: ransomware, infostealers, remote access trojans, cryptominers. The 7% decline reflects media sophistication, not decreased threat. Coverage now clusters around novel malware families (new techniques) rather than cataloging every variant.",
        "expert_take": "The last time 'malware' spiked in general interest coverage was during major wormable threats (WannaCry era). Now it's specialty trade press vocabulary. This linguistic evolution actually helps—forcing more precise threat communication. Though it makes trend analysis harder when terminology keeps shifting."
    },
    {
        "keyword": "Data Breach",
        "current_count": 520,
        "previous_count": 478,
        "change_percent": 8.8,
        "trend": "rising",
        "sentiment": "negative",
        "days_active": 30,
        "peak_date": "2025-09-08",
        "narrative": "Data breach coverage grew 9% despite breach fatigue setting in years ago. What changed? Regulatory teeth. SEC disclosure requirements, GDPR enforcement actions, and class-action lawsuits transformed breaches from 'unfortunate incidents' to 'board-level liability events.' Media now covers the aftermath as much as the breach itself.",
        "expert_take": "The interesting pattern: breaches affecting 100M+ records barely register anymore unless there's a unique angle (vulnerable population, novel attack vector, executive negligence). Meanwhile, breaches of 10K records at healthcare or government entities generate sustained coverage due to data sensitivity. Volume no longer determines newsworthiness—context does."
    },
    {
        "keyword": "Cybercrime",
        "current_count": 549,
        "previous_count": 531,
        "change_percent": 3.4,
        "trend": "stable",
        "sentiment": "negative",
        "days_active": 30,
        "peak_date": "2025-09-23",
        "narrative": "Steady 3.4% growth in 'cybercrime' coverage reflects law enforcement's PR efforts—agency press releases increasingly use this framing to position cyber threats within traditional crime narratives that policymakers and public understand. FBI, Interpol, Europol all pushing 'cybercrime' terminology to justify budget requests and international cooperation frameworks.",
        "expert_take": "Notice how 'cybercrime' dominates when covering threat actor arrests, dark web marketplace takedowns, and cryptocurrency theft. It's law enforcement language, not security industry language. This linguistic split reveals whose narrative is being amplified—and whose concerns (nation-state espionage, corporate espionage) get minimized in mainstream coverage."
    },
    {
        "keyword": "Deepfake",
        "current_count": 318,
        "previous_count": 216,
        "change_percent": 47.2,
        "trend": "surging",
        "sentiment": "concerning",
        "days_active": 30,
        "peak_date": "2025-10-10",
        "narrative": "The 47% surge in deepfake coverage represents the single most dramatic narrative shift in cybersecurity journalism this year. We're witnessing real-time evolution from academic curiosity (2023) to sci-fi speculation (2024) to documented business threat (2025). October 10 peak coincided with Australian Electoral Commission warnings—the moment deepfakes entered mainstream political discourse, not just tech coverage.",
        "expert_take": "What's fascinating: deepfake coverage now splits three ways. One-third discusses election integrity (political journalists). One-third covers fraud and impersonation (business journalists). One-third focuses on detection technology (tech journalists). No consensus on framing yet, which means the narrative is still forming. First movers in thought leadership have maybe 90 days before the narrative crystallizes and everyone has an opinion."
    },
    {
        "keyword": "Social Engineering",
        "current_count": 300,
        "previous_count": 289,
        "change_percent": 3.8,
        "trend": "stable",
        "sentiment": "negative",
        "days_active": 29,
        "peak_date": "2025-09-26",
        "narrative": "'Social engineering' is quietly absorbing phishing, pretexting, and now deepfake attacks under its umbrella. The 4% growth seems modest until you realize this represents fundamental reclassification of attack vectors. What was once 'phishing email' is now 'multi-channel social engineering campaign.' The sophistication implied by this terminology shift is significant.",
        "expert_take": "Security professionals have used 'social engineering' for decades, but its mainstream media adoption is new. Journalists discovered they can use one term instead of explaining phishing, vishing, smishing, quishing, etc. This linguistic efficiency actually improves public understanding—framing everything as manipulation of human psychology rather than technical exploitation."
    },
    {
        "keyword": "Threat Actor",
        "current_count": 325,
        "previous_count": 291,
        "change_percent": 11.7,
        "trend": "rising",
        "sentiment": "analytical",
        "days_active": 30,
        "peak_date": "2025-09-29",
        "narrative": "The 12% increase in 'threat actor' usage signals journalism's professionalization. Five years ago, media said 'hackers.' Three years ago, 'hacking groups.' Now, 'threat actors'—the terminology of intelligence analysts. This isn't just vocabulary change; it reflects growing media understanding of attribution complexity and the spectrum from opportunistic criminals to nation-state operators.",
        "expert_take": "When Bloomberg and Financial Times start using 'threat actor' instead of 'hacker,' it means cybersecurity has achieved legitimate business journalism status. This matters because language shapes perception—'hacker' implies lone wolf, 'threat actor' implies organized operation requiring organizational response, not just technical defense."
    },
    {
        "keyword": "Zero-Day",
        "current_count": 187,
        "previous_count": 142,
        "change_percent": 31.7,
        "trend": "surging",
        "sentiment": "critical",
        "days_active": 28,
        "peak_date": "2025-10-03",
        "narrative": "Zero-day coverage exploded 32% following several high-profile vulnerability exploitations in September. Media has finally grasped what security professionals have known: zero-days represent the highest-stakes game in cybersecurity. Coverage now emphasizes vendor response times, patch deployment challenges, and the problematic economics of vulnerability disclosure versus exploitation.",
        "expert_take": "The October 3 spike correlates with overlapping disclosures from Microsoft, Cisco, and Oracle—creating a 'perfect storm' news cycle where journalists could write about zero-days as a systemic problem rather than isolated incidents. This thematic coverage is more dangerous to vendors than individual bug reports because it questions the sustainability of current software development practices."
    }
]

# Weekly breakdown for top keywords
weekly_keyword_data = {
    "weeks": ["Aug 18", "Aug 25", "Sep 1", "Sep 8", "Sep 15", "Sep 22", "Sep 29", "Oct 6", "Oct 13"],
    "keywords": {
        "Cyberattack": [98, 119, 234, 203, 283, 329, 262, 198, 77],
        "Ransomware": [99, 133, 202, 188, 156, 250, 156, 160, 62],
        "Phishing": [133, 131, 276, 205, 220, 191, 123, 117, 35],
        "Malware": [93, 77, 213, 156, 138, 193, 97, 125, 48],
        "Data Breach": [64, 111, 144, 132, 115, 132, 119, 129, 60],
        "Deepfake": [12, 18, 31, 42, 56, 78, 89, 102, 124]
    }
}

# ============================================================================
# SENTIMENT ANALYSIS DATA
# ============================================================================

sentiment_timeline = [
    {"date": "2025-09-15", "negative": 0.68, "neutral": 0.24, "positive": 0.08},
    {"date": "2025-09-18", "negative": 0.71, "neutral": 0.22, "positive": 0.07},
    {"date": "2025-09-21", "negative": 0.65, "neutral": 0.27, "positive": 0.08},
    {"date": "2025-09-24", "negative": 0.73, "neutral": 0.20, "positive": 0.07},
    {"date": "2025-09-27", "negative": 0.69, "neutral": 0.23, "positive": 0.08},
    {"date": "2025-09-30", "negative": 0.66, "neutral": 0.26, "positive": 0.08},
    {"date": "2025-10-03", "negative": 0.75, "neutral": 0.19, "positive": 0.06},
    {"date": "2025-10-06", "negative": 0.70, "neutral": 0.23, "positive": 0.07},
    {"date": "2025-10-09", "negative": 0.72, "neutral": 0.21, "positive": 0.07},
    {"date": "2025-10-12", "negative": 0.68, "neutral": 0.24, "positive": 0.08},
]

# ============================================================================
# ORGANIZATIONS DATA
# ============================================================================

top_organizations = [
    {
        "name": "Jaguar Land Rover",
        "mentions": 420,
        "incident_type": "Supply Chain Attack",
        "first_seen": "2025-09-18",
        "coverage_intensity": "very_high",
        "industry": "Automotive",
        "narrative": "JLR's breach dominated coverage for three weeks straight—not because of technical sophistication, but because it hit during peak production cycles, causing visible delays in vehicle deliveries. British media coverage was relentless: every update on factory status became a new story. Scattered Spider's targeting demonstrates threat actors' strategic shift toward high-visibility brands where operational disruption creates media and shareholder pressure.",
        "why_it_matters": "This incident revealed how automotive manufacturing's just-in-time supply chains amplify cyber incident impacts. A single compromised supplier portal cascaded into production halts across multiple facilities. Coverage emphasized tangible business consequences (missed delivery dates, revenue loss, stock price decline) over technical attack details—the kind of framing that gets board attention."
    },
    {
        "name": "Collins Aerospace",
        "mentions": 361,
        "incident_type": "Data Breach",
        "first_seen": "2025-09-20",
        "coverage_intensity": "high",
        "industry": "Aerospace & Defense",
        "narrative": "When a military contractor suffers a data breach, coverage splits between business impact and national security implications. Collins Aerospace got both: aviation industry trades covered operational concerns while defense journalists explored potential classified information exposure. The sustained coverage (361 articles) reflects the complexity of aerospace supply chains—every airline using Collins components wanted reassurance.",
        "why_it_matters": "Defense contractor breaches rarely generate this much coverage unless they have clear commercial aviation angles. Collins straddles military and commercial, making it newsworthy to multiple journalist specializations. The incident also coincided with broader DOD discussions about supply chain security requirements, giving reporters a ready-made policy context hook."
    },
    {
        "name": "Salesforce",
        "mentions": 193,
        "incident_type": "Platform Vulnerability",
        "first_seen": "2025-09-25",
        "coverage_intensity": "medium",
        "industry": "Technology",
        "narrative": "Salesforce vulnerabilities generate outsized coverage because the platform's market dominance means a single flaw potentially affects thousands of organizations. This wasn't a breach but a vulnerability disclosure—yet 193 articles covered it because every company using Salesforce suddenly had an action item. Coverage focused on patch timelines and whether organizations actually applied updates, a refreshing shift toward defensive accountability.",
        "why_it_matters": "Platform vulnerabilities create coverage velocity that individual company breaches don't, because of multiplier effects. One vulnerability, thousands of potentially affected organizations, each assessing their exposure. This is why SaaS platform security failures get more coverage than on-premise software issues—the blast radius is visible and calculable."
    },
    {
        "name": "Qantas",
        "mentions": 148,
        "incident_type": "Operational Disruption",
        "first_seen": "2025-10-01",
        "coverage_intensity": "medium",
        "industry": "Transportation",
        "narrative": "Qantas incidents generate guaranteed coverage in Australian media due to national carrier status, but this one crossed into international coverage because of its operational visibility. When hundreds of passengers are stranded at airports because of cyber incidents, it makes news. Consumer-facing impacts generate more coverage than backend data breaches—a lesson threat actors seem to have learned.",
        "why_it_matters": "Transportation cybersecurity incidents are the new 'perfect storm' for media coverage: operational disruption (visible to consumers), safety concerns (real or perceived), and business continuity challenges (revenue loss). Qantas coverage demonstrated how cyber incidents affecting physical operations get sustained attention that pure data breaches no longer receive."
    },
    {
        "name": "Brussels Airport",
        "mentions": 116,
        "incident_type": "System Outage",
        "first_seen": "2025-10-05",
        "coverage_intensity": "medium",
        "industry": "Transportation",
        "narrative": "The Brussels Airport incident generated 116 articles despite limited technical details because it paralyzed operations at a major European hub. What's interesting: media couldn't definitively confirm whether it was a cyberattack, ransomware, or system failure—yet covered it extensively anyway. The mere suspicion of cyber involvement was enough. This shows how 'cyber' has become the default explanation for any unexpected technical failure.",
        "why_it_matters": "Critical infrastructure + consumer disruption + European regulatory context = sustained media coverage. The incident occurred during heightened EU discussions about critical infrastructure protection, giving policy journalists a timely hook. Also demonstrates how ambiguity doesn't kill stories—if anything, speculative 'cyber incident or not?' coverage generates more articles than confirmed technical details."
    },
    {
        "name": "Microsoft",
        "mentions": 130,
        "incident_type": "Multiple Incidents",
        "first_seen": "2025-09-16",
        "coverage_intensity": "medium",
        "industry": "Technology",
        "narrative": "Microsoft's 130 mentions represent not one incident but aggregated coverage of vulnerabilities, patches, Azure outages, and third-party attacks affecting Microsoft services. The company has become infrastructure—when Microsoft has security issues, it's like reporting on electricity grid problems. Coverage is more utility-focused (service continuity) than brand-focused (reputation).",
        "why_it_matters": "Microsoft's omnipresence in coverage reflects its market position: any Microsoft security issue is potentially everyone's problem. The company's security incidents are often covered in business continuity contexts rather than cybersecurity contexts, showing how critical infrastructure framing shapes narrative."
    },
    {
        "name": "Oracle",
        "mentions": 133,
        "incident_type": "Security Advisory",
        "first_seen": "2025-09-22",
        "coverage_intensity": "medium",
        "industry": "Technology",
        "narrative": "Oracle's quarterly security updates reliably generate coverage—not because individual vulnerabilities are newsworthy, but because the sheer volume (often 300+ CVEs per release) raises questions about software security practices. This quarter's 133 articles mostly covered the zero-day vulnerabilities being actively exploited, with critical coverage of Oracle's patch complexity making deployment difficult for enterprises.",
        "why_it_matters": "Oracle coverage illustrates tension between disclosure and deployability. Security researchers praise comprehensive vulnerability disclosure, but system administrators complain that Oracle patches often require extensive testing and create deployment challenges. Media coverage increasingly reflects this practitioner frustration, not just celebrating vulnerability discovery."
    },
    {
        "name": "Discord",
        "mentions": 104,
        "incident_type": "Phishing Campaign",
        "first_seen": "2025-09-28",
        "coverage_intensity": "medium",
        "industry": "Technology",
        "narrative": "Discord's 104 mentions reflect the platform's emergence as both target and vector. Phishing campaigns using Discord's infrastructure, malware distribution through Discord servers, and credential theft targeting Discord accounts all contributed. Coverage split between gaming/tech media (platform security concerns) and cybersecurity media (new attack surface for enterprise threats as Discord gains workplace adoption).",
        "why_it_matters": "Discord represents the blur between consumer and enterprise security. Initially dismissed as gaming platform, it's now used by developer teams, community management, and corporate communications—creating a new attack surface that traditional enterprise security tools don't cover. Media coverage reflects this identity crisis."
    },
    {
        "name": "Asahi Group",
        "mentions": 95,
        "incident_type": "Ransomware",
        "first_seen": "2025-10-08",
        "coverage_intensity": "high",
        "industry": "Food & Beverage",
        "narrative": "Asahi's ransomware incident (Qilin group) generated exceptional coverage for a Japanese company—typically disclosure-averse. The fact that Asahi publicly confirmed the attack, postponed earnings, and provided detailed updates represents a significant shift in Japanese corporate culture around cyber incident transparency. Coverage emphasized business continuity over technical details, with financial analysts assessing operational recovery timelines.",
        "why_it_matters": "This incident may mark a turning point in Asian corporate disclosure norms. Historically, Japanese and Korean companies minimize public discussion of cyber incidents due to reputation concerns. Asahi's transparent approach (forced by ransomware group's public data leak threats) could establish new expectations for incident disclosure in Asian markets."
    },
    {
        "name": "AT&T",
        "mentions": 87,
        "incident_type": "Data Leak",
        "first_seen": "2025-09-19",
        "coverage_intensity": "medium",
        "industry": "Telecommunications",
        "narrative": "AT&T's data leak generated only 87 articles—modest compared to past AT&T incidents affecting 70M+ customers. This muted coverage reflects breach fatigue: unless a telecommunications breach involves novel attack vectors or particularly sensitive data (call records, location data), it barely registers. AT&T has had so many incidents that media treats new breaches as routine operational risks rather than major news events.",
        "why_it_matters": "AT&T's diminished coverage illustrates how repeat incidents create narrative fatigue even for major brands. Media and public have normalized telecommunications breaches to the point where only exceptional circumstances (regulatory penalties, executive accountability, novel attack methods) generate sustained attention. This normalization may reduce public pressure for security improvements—a concerning trend."
    }
]

# ============================================================================
# THREAT ACTORS DATA
# ============================================================================

threat_actors = [
    {
        "name": "Scattered Spider",
        "articles": 251,
        "days_active": 29,
        "targets": ["Jaguar Land Rover", "Multiple Tech Companies"],
        "primary_method": "Social Engineering",
        "sophistication": "high",
        "first_seen": "2025-09-15",
        "coverage_trend": "sustained",
        "profile": "Scattered Spider's 29-day sustained media presence is unprecedented for a threat actor. Most groups get 3-5 day news cycles after incidents; Scattered Spider maintained coverage through continuous target revelations, sophisticated social engineering tactics, and media-savvy operational security. The group's targeting of Jaguar Land Rover—a visible, consumer-facing brand—guaranteed extended coverage as every production update became a new story.",
        "why_notable": "This group represents the evolution of cybercriminal operations toward maximizing media impact. By targeting high-visibility brands and maintaining operational tempo (new victims every few days), they keep their name in coverage, which may serve reputation-building in criminal underground. Their social engineering sophistication also gives journalists compelling human-interest angles beyond technical exploitation.",
        "media_sophistication": "Scattered Spider understands media cycles. They time victim disclosures for maximum attention, provide enough technical details to keep security researchers engaged, but maintain enough mystery to fuel speculation. This is threat actor as performance art—calculated to maintain media interest."
    },
    {
        "name": "Scattered Lapsus$ Hunters",
        "articles": 179,
        "days_active": 27,
        "targets": ["Technology Sector"],
        "primary_method": "Credential Theft",
        "sophistication": "high",
        "first_seen": "2025-09-17",
        "coverage_trend": "increasing",
        "profile": "The 'Scattered Lapsus$ Hunters' naming itself references past incidents, creating brand continuity that media loves. 179 articles over 27 days demonstrates how threat actor branding affects coverage—journalists can reference past incidents, creating narrative continuity that justifies more extensive coverage. The group's targeting of technology companies creates natural media interest in tech journalism circles.",
        "why_notable": "This group's coverage trajectory shows increasing sophistication in media engagement. Early coverage focused on attribution debates (who are they?), middle coverage on tactical methods (how do they operate?), recent coverage on strategic implications (what does this mean for enterprise security?). This narrative evolution demonstrates maturing cybersecurity journalism.",
        "media_sophistication": "By referencing 'Lapsus$' in their naming, they piggyback on extensive past coverage of that group, giving journalists ready-made context. It's threat actor franchising—leveraging brand recognition to amplify media impact of operations."
    },
    {
        "name": "ShinyHunters",
        "articles": 89,
        "days_active": 23,
        "targets": ["E-commerce", "SaaS Platforms"],
        "primary_method": "Database Exploitation",
        "sophistication": "medium",
        "first_seen": "2025-09-20",
        "coverage_trend": "stable",
        "profile": "ShinyHunters generates steady, predictable coverage through volume tactics. Rather than sophisticated targeted attacks, they exploit misconfigurations and exposed databases—then monetize through data broker forums. Coverage focuses less on technical sophistication and more on the underground economy of stolen data. Their 89 articles over 23 days represents consistent low-level media attention rather than dramatic spikes.",
        "why_notable": "ShinyHunters exemplifies the 'commodity breach' economy. Their coverage illustrates how much of cybercrime has become routine business operations—finding exposed databases, scraping data, listing it for sale. Media covers them when specific high-profile databases appear in their listings, but there's little narrative drama because the methods are well-understood.",
        "media_sophistication": "ShinyHunters doesn't court media attention—they operate transactionally. Coverage emerges when security researchers discover their data listings, not through the group's PR efforts. This reactive coverage pattern differs from groups actively managing their media presence."
    },
    {
        "name": "Qilin",
        "articles": 61,
        "days_active": 21,
        "targets": ["Asahi Group", "Food Industry"],
        "primary_method": "Ransomware",
        "sophistication": "high",
        "first_seen": "2025-09-22",
        "coverage_trend": "increasing",
        "profile": "Qilin (also spelled Qilin) is a ransomware-as-a-service operator that generated 61 articles primarily through the high-profile Asahi Group attack. What's interesting: they achieved disproportionate coverage through one major victim rather than many small ones. The Asahi incident's business impact (postponed earnings, operational disruption) gave financial journalists hooks to cover cybersecurity—expanding beyond security trade press.",
        "why_notable": "Qilin demonstrates that in ransomware coverage, victim selection matters more than technical sophistication. One major brand generates more coverage than dozens of small businesses. Their targeting of food/beverage industry also unusual—most ransomware groups focus on healthcare, government, financial services. This sector diversification caught media attention as novel pattern.",
        "media_sophistication": "Qilin's leak site is professionally designed with countdown timers and detailed victim profiles—pure psychological warfare designed to pressure payment and generate media interest. Their public data releases are staged for maximum dramatic impact, understanding that media coverage increases pressure on victims."
    },
    {
        "name": "Kimsuky",
        "articles": 59,
        "days_active": 14,
        "targets": ["Government", "Think Tanks"],
        "primary_method": "Spear Phishing",
        "sophistication": "high",
        "first_seen": "2025-10-01",
        "coverage_trend": "emerging",
        "profile": "Kimsuky's 59 articles over just 14 days represents intense coverage velocity—multiple articles per day. This APT group's coverage benefits from nation-state attribution (North Korea), giving journalists geopolitical framing that elevates cybersecurity incidents into international relations stories. Coverage emphasizes intelligence gathering objectives over financial motivation, distinguishing it from criminal ransomware coverage.",
        "why_notable": "Kimsuky's October emergence in coverage correlates with heightened geopolitical tensions and upcoming policy discussions. Media coverage of APT groups often spikes when their operations align with broader news cycles (elections, international summits, policy debates). The group has operated for years, but media attention comes in waves triggered by contextual relevance.",
        "media_sophistication": "State-sponsored groups like Kimsuky don't court media attention—their coverage is driven by threat intelligence firms' research publications and government attribution statements. This creates 'authoritative source' coverage that differs from criminal group speculation. Journalists treat nation-state threat actors as legitimate security threats rather than criminal enterprises."
    },
    {
        "name": "Lazarus Group",
        "articles": 43,
        "days_active": 16,
        "targets": ["Financial Services", "Cryptocurrency"],
        "primary_method": "APT Operations",
        "sophistication": "very_high",
        "first_seen": "2025-09-25",
        "coverage_trend": "stable",
        "profile": "Lazarus Group's relatively modest 43 articles belies their significance—they're arguably the most sophisticated threat actor in operation today. Lower article counts reflect coverage fatigue: Lazarus has been active for over a decade, so unless they pull off something spectacular (like the $600M+ cryptocurrency heist in 2023), media treats their operations as routine. The 16-day coverage window likely corresponds to a specific campaign or attribution announcement.",
        "why_notable": "Lazarus coverage illustrates how even highly sophisticated threat actors face media normalization. Their technical capabilities are exceptional, but journalists need fresh angles to justify coverage. Financial services targeting generates some attention, but cryptocurrency theft has become almost expected from this group. Coverage now focuses more on attribution methods and geopolitical implications than technical tactics.",
        "media_sophistication": "As a nation-state group, Lazarus doesn't engage with media directly. Their coverage is entirely driven by security researcher analysis and government statements. However, their operational security has improved over years—they leave fewer forensic breadcrumbs, making attribution stories more speculative and thus generating less confident coverage."
    },
    {
        "name": "Cl0p / Clop",
        "articles": 81,
        "days_active": 18,
        "targets": ["Enterprise Software Users"],
        "primary_method": "Ransomware",
        "sophistication": "high",
        "first_seen": "2025-09-18",
        "coverage_trend": "declining",
        "profile": "Cl0p's 81 articles represent declining coverage from their peak during the MOVEit vulnerability exploitation campaign (2023-2024). The group pioneered 'mass exploitation' ransomware tactics—find a vulnerability in widely-used enterprise software, exploit it at scale, ransom hundreds of victims simultaneously. This industrial approach generates initial coverage spikes but then fatigue as each new victim becomes routine.",
        "why_notable": "Cl0p's coverage trajectory demonstrates how threat actor tactics affect media sustainability. Their mass exploitation approach generates brief intense coverage (when vulnerability announced) followed by long tail of individual victim stories that few outlets cover comprehensively. Compare to targeted attacks (like Scattered Spider) which generate sustained narrative arcs around each victim.",
        "media_sophistication": "Cl0p's leak site was one of the first professionally designed ransomware shaming portals, establishing practices now industry-standard: countdown timers, victim profiles, data samples. They understood media mechanics before most groups—creating pressure through public exposure, not just encryption. Their declining coverage reflects market saturation of these tactics, not decreased activity."
    }
]

# ============================================================================
# INDUSTRY SECTOR DATA
# ============================================================================

industry_distribution = [
    {
        "industry": "Technology",
        "article_count": 4015,
        "change_percent": 8.2,
        "avg_severity": "high",
        "insight": "Technology's dominance in coverage (4,015 articles) isn't just because tech companies get attacked more—it's because tech journalists understand cybersecurity better than other beat reporters. When a bank gets breached, business journalists cover it as financial news. When a tech company gets breached, tech journalists cover it as security news with actual technical detail. This creates self-reinforcing coverage concentration.",
        "trend_note": "The 8.2% growth is actually slowing compared to previous periods. Technology is losing coverage share to critical infrastructure and manufacturing—not because attacks decreased, but because journalists are discovering cybersecurity angles in traditionally non-tech sectors."
    },
    {
        "industry": "Financial Services",
        "article_count": 2051,
        "change_percent": 5.3,
        "avg_severity": "critical",
        "insight": "Financial services maintains steady coverage (2,051 articles, +5.3%) because these incidents trigger regulatory reporting requirements that generate public documentation. SEC filings, banking regulator statements, and earnings call mentions create paper trails that journalists can reference. This structural transparency sustains coverage even when organizations try to minimize publicity.",
        "trend_note": "Coverage emphasizes regulatory consequences over technical details. When financial institutions face cybersecurity incidents, media focuses on compliance failures, customer compensation, and regulatory penalties—business journalism framing rather than security journalism framing."
    },
    {
        "industry": "Government",
        "article_count": 1358,
        "change_percent": 12.7,
        "avg_severity": "high",
        "insight": "Government sector coverage surged 12.7% (1,358 articles), driven by election security concerns, critical infrastructure protection debates, and several high-profile incidents (German procurement portal, Australian electoral commission warnings). Government incidents blend cybersecurity with political journalism—expanding coverage beyond tech press into mainstream political coverage.",
        "trend_note": "The interesting pattern: government incidents generate more coverage in countries with active cybersecurity policy debates. German government hack got extensive coverage because it fed ongoing discussions about digital sovereignty and infrastructure protection. Same incident in a country without active cyber policy discourse might generate a fraction of the coverage."
    },
    {
        "industry": "Critical Infrastructure",
        "article_count": 887,
        "change_percent": 15.4,
        "avg_severity": "critical",
        "insight": "Critical infrastructure's 15.4% growth (887 articles) reflects media's growing understanding that these incidents have physical-world consequences. When airports, power grids, or water systems face cyber incidents, coverage emphasizes public safety and operational continuity—hooks that generate sustained attention beyond security implications alone.",
        "trend_note": "Transportation dominated critical infrastructure coverage this period (Brussels Airport, Qantas, Heathrow), creating narrative cluster around aviation cybersecurity. Media loves these stories because operational disruption is visible and photographable—stranded passengers, delayed flights, airport chaos. Much more compelling than backend IT system breaches."
    },
    {
        "industry": "Healthcare",
        "article_count": 661,
        "change_percent": 3.2,
        "avg_severity": "critical",
        "insight": "Healthcare's modest 3.2% growth (661 articles) is concerning given that ransomware groups heavily target this sector. The muted coverage reflects normalization—healthcare breaches have become so routine that only exceptional cases (patient deaths attributed to ransomware, massive hospital system shutdowns) generate significant attention. This normalization may reduce pressure for security improvements.",
        "trend_note": "Healthcare coverage increasingly emphasizes patient care disruption over data breaches. Journalists have learned that 'surgery postponed due to ransomware' generates more reader engagement than 'patient records exposed.' This framing shift actually helps public understanding of cybersecurity's real-world impacts."
    },
    {
        "industry": "Manufacturing",
        "article_count": 618,
        "change_percent": 23.1,
        "avg_severity": "medium",
        "insight": "Manufacturing's explosive 23.1% growth (618 articles) represents the year's most under-reported major trend. Driven partly by Jaguar Land Rover incident (420 articles alone), but broader pattern of industrial control system targeting, supply chain disruptions, and just-in-time manufacturing vulnerability to cyber incidents. Media is discovering manufacturing cybersecurity, but coverage still lags threat landscape.",
        "trend_note": "Most manufacturing coverage comes from industry trade press, not general business media—limiting audience reach. When manufacturing cybersecurity breaks into mainstream coverage (like JLR), it's framed as supply chain story or business continuity story, rarely as cybersecurity story. This categorization affects which journalists cover it and how deeply."
    },
    {
        "industry": "Retail/E-commerce",
        "article_count": 501,
        "change_percent": 1.8,
        "avg_severity": "medium",
        "insight": "Retail's near-flat growth (501 articles, +1.8%) reflects coverage fatigue with payment card breaches and credential stuffing attacks. Unless a breach affects a major brand during peak shopping season (holiday, back-to-school), retail cybersecurity incidents barely register. The sector has normalized frequent low-level compromises to the point where media considers them unremarkable.",
        "trend_note": "E-commerce coverage differs from physical retail: online platforms get covered as 'technology' companies, physical retailers get covered as 'retail' breaches. This classification affects coverage depth—technology journalists provide technical analysis, retail journalists focus on customer impact and brand reputation."
    },
    {
        "industry": "Education",
        "article_count": 398,
        "change_percent": -4.2,
        "avg_severity": "low",
        "insight": "Education sector's 4.2% decline (398 articles) corresponds to summer period where school breaches generate less attention. But the trend also reflects structural issues: education institutions rarely have PR resources to manage incident communications, creating information vacuums that journalists struggle to fill. Coverage is often delayed, incomplete, and lacks technical detail.",
        "trend_note": "K-12 education breaches get minimal coverage despite affecting minors—surprisingly low given media's usual emphasis on child safety. University breaches get more coverage, especially research universities where industrial espionage angles attract attention. This disparity may reflect journalist access to university PR offices versus limited K-12 district communication capacity."
    },
    {
        "industry": "Transportation",
        "article_count": 238,
        "change_percent": 31.5,
        "avg_severity": "high",
        "insight": "Transportation's 31.5% surge (238 articles) marks it as the fastest-growing sector in coverage. High-visibility operational disruptions (Brussels Airport, Qantas, Heathrow) created sustained news cycles because incidents affected thousands of consumers directly. This sector's coverage velocity suggests it may become the 'poster child' for critical infrastructure cybersecurity in media narratives.",
        "trend_note": "Transportation incidents get covered by travel journalists, business journalists, and security journalists simultaneously—creating coverage multiplication effect. Same incident generates distinct articles from each journalism specialty, inflating coverage volume beyond single-specialty sectors."
    },
    {
        "industry": "Telecommunications",
        "article_count": 116,
        "change_percent": 6.9,
        "avg_severity": "high",
        "insight": "Telecommunications' steady 6.9% growth (116 articles) masks saturation and fatigue. Major telecom breaches (AT&T, T-Mobile, Verizon historically) have become so frequent that new incidents barely generate coverage unless involving particularly sensitive data (call records, location data, real-time communications). The sector has normalized breaches to an alarming degree.",
        "trend_note": "Telecom coverage increasingly focuses on regulatory response rather than technical incidents. When breaches occur, journalists emphasize FCC responses, congressional inquiries, and class-action lawsuits over the incidents themselves. This procedural focus may reflect media's acceptance that telecom breaches are inevitable, shifting attention to accountability mechanisms."
    }
]

# ============================================================================
# GEOGRAPHIC DATA
# ============================================================================

geographic_distribution = [
    {
        "region": "North America",
        "article_count": 2940,
        "percentage": 30.8,
        "trend": "stable",
        "context": "North America's 2,940 articles (30.8% of total) reflects both high incident frequency and sophisticated cybersecurity journalism infrastructure. US and Canadian media outlets have dedicated security reporters, strong relationships with research firms, and access to organizational spokespeople—creating optimal conditions for comprehensive coverage. However, the 'stable' trend masks a relative decline as other regions catch up in coverage sophistication.",
        "notable": "American exceptionalism in cybersecurity coverage is fading. Five years ago, North America represented 50%+ of global coverage; now it's down to 31%. This shift reflects global diffusion of both cybersecurity threats and journalism capacity to cover them."
    },
    {
        "region": "Global Impact",
        "article_count": 2230,
        "percentage": 23.4,
        "trend": "rising",
        "context": "The 'Global Impact' category (2,230 articles, 23.4%) represents incidents that transcend geography—cloud platform vulnerabilities, supply chain compromises, international threat actor campaigns. This category's growth reflects the reality that in interconnected digital infrastructure, geographic boundaries become meaningless. A vulnerability in a platform used worldwide is simultaneously a risk everywhere.",
        "notable": "Media is slowly learning to frame cybersecurity globally rather than nationally. Instead of 'US company breached,' we're seeing 'global platform compromised affecting users worldwide.' This linguistic shift represents more accurate understanding of digital risk geography—or lack thereof."
    },
    {
        "region": "Europe",
        "article_count": 2012,
        "percentage": 21.1,
        "trend": "rising",
        "context": "Europe's 2,012 articles (21.1%, rising) benefit from GDPR creating mandatory transparency and significant penalties. European breaches generate more sustained coverage because regulatory enforcement creates ongoing story developments—investigation announcements, penalty assessments, appeals. GDPR transformed European cybersecurity incidents from one-off stories into multi-chapter narratives.",
        "notable": "European coverage increasingly emphasizes regulatory and policy angles over technical details. When an organization faces a breach in Europe, journalists focus on GDPR compliance, Data Protection Authority investigations, and potential fines. This regulatory framing may actually improve public understanding by connecting cybersecurity to real business consequences."
    },
    {
        "region": "Asia-Pacific",
        "article_count": 1447,
        "percentage": 15.2,
        "trend": "surging",
        "context": "Asia-Pacific's surging trend (1,447 articles, 15.2%) represents the most significant geographic shift in cybersecurity coverage this year. Driven by increased incident frequency, growing cybersecurity journalism capacity in the region, and high-profile incidents (Asahi Group in Japan, Qantas in Australia). The region's coverage ratio versus North America has shifted from 1:2 to 1:1.8—a dramatic convergence.",
        "notable": "What's remarkable: Japanese media is becoming more transparent about cybersecurity incidents despite traditionally reticent corporate disclosure culture. Korean and Indian cybersecurity journalism is professionalizing rapidly. This regional maturation suggests Asia-Pacific may rival North America in coverage volume within 2-3 years."
    },
    {
        "region": "Australia",
        "article_count": 254,
        "percentage": 2.7,
        "trend": "rising",
        "context": "Australia's 254 articles (tracked separately from broader Asia-Pacific) reflect the country's outsized cybersecurity profile relative to population. Strong regulatory framework (Notifiable Data Breaches scheme), vocal government cybersecurity leadership, and several high-profile incidents (Qantas, electoral commission) create dense coverage. Australian cybersecurity journalism is among the world's most mature.",
        "notable": "Australia's coverage intensity (articles per capita) likely exceeds every other country. This reflects government success in raising cybersecurity awareness and creating transparency expectations. When Australian organizations face breaches, public expects detailed disclosure and accountability—cultural norm not yet universal elsewhere."
    },
    {
        "region": "Africa",
        "article_count": 297,
        "percentage": 3.1,
        "trend": "stable",
        "context": "Africa's 297 articles (3.1%) represents coverage concentrated in South Africa and Nigeria, with limited cybersecurity journalism capacity across most of continent. Much 'African' cybersecurity coverage is actually written by international journalists covering incidents with African dimensions. Building regional cybersecurity journalism capacity remains challenge given resource constraints at media outlets.",
        "notable": "African cybersecurity coverage often emphasizes mobile/fintech incidents over traditional enterprise IT—reflecting the continent's technological leap-frogging. Mobile money platform security generates more coverage than bank breaches, creating coverage patterns distinct from other regions."
    },
    {
        "region": "Latin America & Caribbean",
        "article_count": 171,
        "percentage": 1.8,
        "trend": "declining",
        "context": "Latin America's declining trend (171 articles, 1.8%) reflects both limited cybersecurity journalism infrastructure and corporate disclosure norms that minimize public incident discussion. Many incidents occur but don't generate coverage because organizations avoid public disclosure and journalists lack resources to investigate independently. This coverage gap creates dangerous information asymmetry.",
        "notable": "Brazilian cybersecurity coverage dominates the regional total, with limited journalism in other Latin American countries. This concentration means most regional cybersecurity discourse happens in Portuguese, creating linguistic barriers to hemispheric information sharing."
    },
    {
        "region": "Middle East",
        "article_count": 111,
        "percentage": 1.2,
        "trend": "stable",
        "context": "Middle East's 111 articles (1.2%) represents both limited incidents becoming public and restricted cybersecurity journalism. Nation-state cyber operations in the region rarely generate coverage from domestic media, while international coverage focuses on geopolitical dimensions rather than technical details. The region's cybersecurity discourse is heavily securitized—focused on warfare rather than enterprise security.",
        "notable": "UAE and Israel account for majority of Middle Eastern cybersecurity coverage, reflecting those nations' technology sector development and relatively open media environments. Coverage from other regional countries is sparse, often focused on government announcements rather than incident reporting."
    }
]

# ============================================================================
# TECHNICAL METHODS DATA
# ============================================================================

technical_methods = [
    {
        "method": "Malware Deployment",
        "count": 3246,
        "severity": "high",
        "trend": "stable",
        "detail": "Malware deployment's 3,246 mentions reflect its status as attack method umbrella term—covering ransomware, infostealers, backdoors, trojans, and everything in between. The 'stable' trend masks internal category shifts: ransomware mentions declining while infostealer mentions rising. Media gradually learning to use specific malware categories rather than generic 'malware,' improving coverage precision.",
        "expert_note": "When journalists say 'malware deployed,' it often means they lack specific technical details about the attack. More sophisticated coverage specifies malware family, delivery mechanism, and capabilities. The persistence of generic 'malware' terminology indicates ongoing technical knowledge gaps in broader journalism."
    },
    {
        "method": "Phishing Vector",
        "count": 3114,
        "severity": "high",
        "trend": "declining",
        "detail": "Phishing vector's 3,114 mentions (declining trend) creates misleading impression that phishing is decreasing. Reality: phishing is being reclassified as 'social engineering,' 'business email compromise,' 'credential theft,' etc. The attack method hasn't declined—media vocabulary evolved beyond single-term categorization. Modern phishing campaigns too sophisticated for simple 'phishing' label.",
        "expert_note": "The 'phishing' terminology crisis: security professionals distinguish between email phishing, smishing, vishing, spear-phishing, whaling, etc. Journalists struggle with this taxonomy, so often default to 'phishing' even when attack used multiple vectors. This linguistic imprecision obscures attack sophistication from public understanding."
    },
    {
        "method": "Unpatched Vulnerability",
        "count": 1366,
        "severity": "critical",
        "trend": "rising",
        "detail": "Unpatched vulnerability exploitation's rising trend (1,366 mentions) reflects two factors: more zero-days being actively exploited, and media finally understanding that patch deployment failures are newsworthy. Coverage increasingly emphasizes organizational failure to patch (accountability framing) versus just technical vulnerability existence. This shift toward defensive accountability improves public discourse.",
        "expert_note": "The growing focus on 'unpatched' vulnerabilities represents journalism maturation. Early cybersecurity coverage celebrated researchers discovering vulnerabilities; current coverage questions why organizations haven't deployed available patches. This reframing from offensive to defensive perspective makes cybersecurity coverage more actionable for practitioners."
    },
    {
        "method": "Stolen Credentials",
        "count": 989,
        "severity": "high",
        "trend": "rising",
        "detail": "Stolen credentials' rising trend (989 mentions) reflects the method's emergence as primary initial access vector, surpassing vulnerability exploitation in many contexts. Credential theft feeds credential stuffing, account takeover, and lateral movement—making it force multiplier for subsequent attack stages. Coverage growth indicates media understanding that authentication is the new perimeter.",
        "expert_note": "Stolen credentials coverage often overlooks the supply chain: where did credentials come from? Usually answer is previous breaches, infostealer malware, or phishing campaigns—meaning 'stolen credentials' is endpoint of different attack, not standalone method. Media rarely traces this attribution chain, treating credentials as mysteriously appearing on dark web markets."
    },
    {
        "method": "Social Engineering",
        "count": 469,
        "severity": "medium",
        "trend": "rising",
        "detail": "Social engineering's 469 mentions (rising) represents the category absorbing phishing, pretexting, and now deepfake attacks. This consolidation improves conceptual understanding—framing attacks as psychological manipulation rather than technical exploitation. Coverage increasingly emphasizes human factors and organizational culture over technical controls, though implementation advice remains limited.",
        "expert_note": "The shift toward 'social engineering' terminology helps and hurts. Helps: focuses attention on human vulnerabilities and need for security culture. Hurts: becomes catch-all that obscures tactical differences between email phishing, vishing with deepfake audio, and in-person pretexting. Specificity matters for defensive guidance."
    },
    {
        "method": "Authentication Bypass",
        "count": 422,
        "severity": "critical",
        "trend": "stable",
        "detail": "Authentication bypass's 422 mentions (stable) covers everything from brute force attacks to MFA fatigue exploitation to session hijacking. The stable trend belies growing sophistication—attackers increasingly bypass rather than break authentication. Coverage emphasizes that authentication is not binary (authenticated vs. not); it's continuous verification challenge that organizations are losing.",
        "expert_note": "Authentication bypass coverage reveals technical literacy gaps. Journalists often describe attacks as 'bypassing security' without explaining how—treating authentication like a binary gate that's either open or closed. Reality is complex: partial authentication, privilege escalation, session management failures. Simplification aids readability but obscures defensive lessons."
    },
    {
        "method": "Data Exfiltration",
        "count": 113,
        "severity": "high",
        "trend": "stable",
        "detail": "Data exfiltration's modest 113 mentions indicates it's rarely covered as standalone attack phase—usually mentioned as outcome of other attacks (breach → exfiltration) rather than distinct method. This bundling misses important story: how attackers move large data volumes without detection. Coverage gap in network monitoring, data loss prevention failures, and detection challenges.",
        "expert_note": "Data exfiltration's low coverage reflects journalists' focus on access (how attackers got in) over actions on objectives (what they did once inside). This access-centric framing misses that many breaches involve extended dwell time where exfiltration detection failures are the real defensive breakdown, not initial access."
    },
    {
        "method": "Ransomware",
        "count": 83,
        "severity": "critical",
        "trend": "declining",
        "detail": "Ransomware's surprisingly low 83 mentions as 'method' (versus 761 as 'threat category') shows classification confusion. Ransomware is both attack method and criminal business model, creating taxonomic ambiguity in coverage. The declining trend likely reflects media's shift toward covering ransomware as organizational crisis rather than technical attack—emphasis moving from 'how' to 'what now.'",
        "expert_note": "Ransomware's coverage evolution mirrors cybersecurity's business mainstreaming. Five years ago: technical analysis of encryption algorithms. Three years ago: ransom payment debates. Now: business continuity, cyber insurance, regulatory reporting. Coverage moved from IT department concern to board-level crisis. This elevation improved organizational attention but reduced technical understanding."
    },
    {
        "method": "DDoS Attack",
        "count": 49,
        "severity": "medium",
        "trend": "declining",
        "detail": "DDoS attacks' declining coverage (49 mentions) reflects normalization and commoditization. Unless DDoS takes down major platforms (rare with modern mitigation), it barely generates coverage. Small-scale DDoS treated as routine operational challenges rather than newsworthy security incidents. This normalization possibly dangerous—organizations may under-invest in DDoS mitigation assuming media attention correlates with business risk.",
        "expert_note": "DDoS coverage decline shows how attack method maturity affects newsworthiness. DDoS is well-understood, mitigation is commoditized, incidents are frequent—creating 'dog bites man' dynamic where coverage only occurs with exceptional scale or targets. This creates dangerous perception that DDoS is 'solved problem' despite ongoing operational impacts."
    }
]

# ============================================================================
# AI-GENERATED INSIGHTS (STATIC TEXT)
# ============================================================================

executive_summary = """
**Strategic Coverage Intelligence – Last 30 Days**

Three seismic shifts are reshaping cybersecurity's media landscape, and they're happening faster than most organizations realize:

**1. The Deepfake Revolution is Here (And It's Not What We Expected)**

Deepfake coverage didn't just grow—it exploded with 47% week-over-week acceleration, the fastest threat narrative expansion we've ever tracked. But here's what's fascinating: this isn't driven by technical breakthroughs. The technology has existed for years. What changed is the *deployment context*.

The Australian Electoral Commission's October warnings about deepfakes threatening election integrity pushed this from cybersecurity trade press into mainstream political coverage. Suddenly, deepfakes aren't a future technology risk—they're a present democracy threat. This reframing transformed media coverage from "can this happen?" to "how do we defend against this?"

For thought leadership: You have maybe 90 days before this narrative hardens and everyone has an opinion. Right now, there's genuine confusion about defensive strategies beyond detection (which everyone agrees will always lag creation). The opportunity is in strategic frameworks, not technical tools.

**2. Critical Infrastructure Coverage Has Overtaken Enterprise IT (And It's Personal Now)**

Transportation and manufacturing incidents (Jaguar Land Rover, Brussels Airport, Qantas, Heathrow) generated more sustained coverage than the entire financial services sector. Why? Because these attacks have *visible* consequences.

When ransomware hits a hospital, it's a data breach. When ransomware hits an airport, thousands of passengers are stranded, photographed, interviewed. When it hits an automotive manufacturer, car deliveries get delayed, shareholders get angry, workers get sent home. Media loves these stories because operational disruption creates human-interest angles that data breaches never will.

This visibility gap is changing threat actor behavior. Scattered Spider's targeting of Jaguar Land Rover wasn't random—it was strategic. High-visibility targets create media pressure that accelerates ransom payment decisions. Threat actors have figured out that media attention is leverage.

For thought leadership: The market is saturated with "data breach response" guidance. It's undersupplied with "operational continuity under cyber crisis" frameworks. Organizations need to understand that cyber incidents are increasingly judged by operational impact, not data sensitivity.

**3. Threat Actor Branding is Now a Media Strategy (And It's Working)**

Scattered Spider maintained 29 consecutive days of media coverage—unprecedented for a threat actor. Most groups get 3-5 day news cycles after incidents. How did they do it? By understanding media mechanics.

They time victim disclosures for maximum attention. They release just enough technical details to keep security researchers engaged but maintain enough mystery to fuel ongoing speculation. They target high-visibility brands that guarantee news coverage. They're not just running cybercrime operations—they're managing media presence.

This represents threat actor evolution: from anonymous "hackers" to branded entities with consistent media strategies. Groups like "Scattered Lapsus$ Hunters" literally name themselves to piggyback on previous coverage, creating narrative continuity that journalists love because it provides ready-made context.

For thought leadership: Organizations think about cyber PR reactively (how to respond when breached). They should think about it proactively: threat actors are already managing media narratives around incidents—sometimes better than victim organizations. The communications game is changing, and most organizations haven't noticed yet.

**What This Means for Your Strategy:**

The cybersecurity narrative is shifting from technical incidents to business crises, from data breaches to operational disruptions, from anonymous threats to branded adversaries. Organizations still preparing for yesterday's media environment will be blindsided by today's coverage patterns.

The opportunity: These shifts create genuine confusion in the market. No one has figured out best practices yet. First movers in strategic guidance (not technical tools) will establish authority that lasts years.
"""

# Due to length constraints, I'll provide the key_insights structure but abbreviated. In your actual file, these would be the full 2000+ word versions from the artifact.

key_insights = [
    {
        "title": "The Deepfake Threshold: When AI Threats Became Mainstream Reality",
        "category": "Emerging Threat",
        "confidence": "Very High",
        "description": "Deepfake coverage exploded 47% WoW, representing transition from theoretical risk to documented attack vector. Australian Electoral Commission warnings pushed this from tech media to mainstream political coverage, marking the moment AI-enabled threats entered public consciousness beyond cybersecurity specialists...",
        "recommendation": "Position as early expert in AI-enabled social engineering defense. Market saturated with detection technology coverage but lacks strategic frameworks for organizational resilience. Content angle: 'Beyond Detection: Building AI-Resistant Security Culture'. Timeline: 90-day window before market saturates.",
        "data_points": [
            "318 articles in 30 days (+47% WoW)",
            "30 consecutive days of coverage",
            "Coverage expanded to 16% mainstream news outlets",
            "Peak: Oct 10 (43 articles in single day)"
        ]
    },
    # Additional insights would follow the same structure...
]

coverage_shifts = [
    "**Deepfake coverage velocity:** +47% WoW – fastest-growing threat narrative in tracking history",
    "**Phishing coverage collapse:** -70% in single week (Sep 29: 123 → Oct 13: 35 articles)",
    "**Manufacturing sector emergence:** +23.1% coverage growth, yet remains under-analyzed in thought leadership",
    "**Geographic rebalancing:** Asia-Pacific coverage growth outpacing North America (ratio shift 1:2 → 1:1.8)",
    "**Transportation sector dominance:** +31.5%, surpassing healthcare in coverage volume",
    "**Threat actor mainstreaming:** Named groups appearing in 34% more general business publications"
]

# ============================================================================
# CHAT INTERFACE Q&A RESPONSES
# ============================================================================

# This is a large dictionary - including abbreviated version here
# In your actual file, use the full responses from the artifact

chat_responses = {
    "trending": {
        "query_variants": ["what are the trending topics", "what's trending", "top trends"],
        "response": "Based on coverage analysis, here are the fastest-growing cybersecurity narratives:\n\n1. **Deepfake Security Threats** (+47% WoW)...\n[Full response would be here]"
    },
    "threat_actors": {
        "query_variants": ["threat actors", "who are the hackers", "active groups"],
        "response": "**Most Active Threat Actors:**\n\n**1. Scattered Spider** - 251 articles over 29 days...\n[Full response would be here]"
    },
    # Add all other categories from the artifact...
}

default_chat_response = """
I can help you explore cybersecurity coverage intelligence! Here are some areas I can analyze:

🔍 **Available Analysis:**
- **Trending Topics:** Fastest-growing threat narratives and emerging patterns
- **Threat Actors:** Active groups, campaign analysis, attribution trends
- **Organizations:** Coverage patterns, industry targeting, incident types
[...]

What would you like to explore?
"""

# ============================================================================
# RECENT INCIDENTS DATA
# ============================================================================

recent_incidents_detailed = [
    {
        "date": "2025-10-15",
        "organization": "Noosa Shire Council",
        "country": "Australia",
        "incident_type": "Business Email Compromise",
        "threat_actor": "International criminal gang",
        "impact_description": "$2.3M fraud during 2024 Christmas period",
        "article_count": 8,
        "coverage_tone": "Public sector vulnerability focus",
        "narrative": "Small Australian council losing $2.3M demonstrates that sophisticated fraud doesn't require technical sophistication..."
    },
    # Add all other incidents from artifact...
]

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

summary_stats = {
    "total_articles_analyzed": 6332,
    "previous_period_articles": 5651,
    "percent_change": 12.1,
    "active_threat_narratives": 47,
    "unique_organizations": 250,
    "fortune_500_percentage": 20,
    "avg_daily_articles": 211,
    "unique_media_outlets": 1243,
    "geographic_regions_covered": 8,
    "industry_sectors_tracked": 15,
    "identified_threat_actors": 67,
    "coverage_date_range": "Sept 15 - Oct 14, 2025"
}

# ============================================================================
# HELPER FUNCTION
# ============================================================================


def get_chart_data(chart_type):
    """Returns properly formatted data for different chart types"""
    if chart_type == "daily_volume":
        return daily_articles
    elif chart_type == "keyword_trends":
        return keyword_trends
    elif chart_type == "weekly_trends":
        return weekly_keyword_data
    elif chart_type == "sentiment":
        return sentiment_timeline
    elif chart_type == "organizations":
        return top_organizations
    elif chart_type == "threat_actors":
        return threat_actors
    elif chart_type == "industries":
        return industry_distribution
    elif chart_type == "geography":
        return geographic_distribution
    elif chart_type == "methods":
        return technical_methods
    else:
        return None

# ============================================================================
#
# ============================================================================
# EXPORT ALL DATA
# ============================================================================


__all__ = [
    'daily_articles',
    'keyword_trends',
    'weekly_keyword_data',
    'sentiment_timeline',
    'top_organizations',
    'threat_actors',
    'industry_distribution',
    'geographic_distribution',
    'technical_methods',
    'executive_summary',
    'key_insights',
    'coverage_shifts',
    'chat_responses',
    'default_chat_response',
    'recent_incidents_detailed',
    'summary_stats',
    'get_chart_data'
]
