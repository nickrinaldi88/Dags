 query = """SELECT DISTINCT tlf.primary_isbn13,
                   campaign_name, 
                   start_date,
                   spend,
                   sales,
                   ACOS,
                   impressions
            FROM title_links_feed tlf
            INNER JOIN itle_campaign tc on tc.primaryisbn13 = title_links_feed.primary_isbn13
            WHERE tc.campaign = 'Amazon - Advertising (paid)'"""
              LEFT JOIN (SELECT primary_isbn13, `
                                ac.name campaign_name,
                                start_date,
                                SUM(spend) spend,
                                ROUND(SUM(sales*0.7),2) sales,
                                ROUND(SUM(spend)/SUM(sales)*100, 2) ACOS,
                                SUM(impressions) impressions
                         FROM adwatch_campaign ac
                           LEFT JOIN adwatch_adgroup ad ON ad.campaign_id = ac.id
                           LEFT JOIN adwatch_product ap ON ap.id = ad.product_id
                           LEFT JOIN adwatch_targeting atar ON ad.adgroup_id = atar.adgroup_id
                           LEFT JOIN adwatch_targeting_performance atp ON atp.targeting_id = atar.id
                         WHERE primary_isbn13 IS NOT NULL
                         GROUP BY primary_isbn13,
                                  start_date,
                                  campaign_name) tc ON tc.primary_isbn13 = tlf.primary_isbn13
            WHERE asin_active = 1
            AND   bisac_status IN ('active','not yet published')
            AND   partner_title = 'N'
            INNER JOIN itle_campaign tc on tc.primaryisbn13 = title_links_feed.primary_isbn13
            WHERE tc.campaign = 'Amazon - Advertising (paid)'"""


'''
(SELECT primary_isbn13, `
                                ac.name campaign_name,
                                start_date,
                                SUM(spend) spend,
                                ROUND(SUM(sales*0.7),2) sales,
                                ROUND(SUM(spend)/SUM(sales)*100, 2) ACOS,
                                SUM(impressions) impressions
                         FROM adwatch_campaign ac
                           LEFT JOIN adwatch_adgroup ad ON ad.campaign_id = ac.id
                           LEFT JOIN adwatch_product ap ON ap.id = ad.product_id
                           LEFT JOIN adwatch_targeting atar ON ad.adgroup_id = atar.adgroup_id
                           LEFT JOIN adwatch_targeting_performance atp ON atp.targeting_id = atar.id
                         WHERE primary_isbn13 IS NOT NULL
                         GROUP BY primary_isbn13,
                                  start_date,
                                  campaign_name) tc ON tc.primary_isbn13 = tlf.primary_isbn13'''