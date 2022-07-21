import math

# def lonlat_to_utm(lon,lat):
#     a = 6378.137
#     earth_radius = 6378137
#     ecc_squared  = 0.00669438
#     k0           = 0.9996
#     f=1/298.257223563 
#     e2=f*(2-f)  
#     E0 = 500
#     N0 = 0
#     Zonenum = int(lon/6) + 31
#     lamda0 = (Zonenum - 1)*6 - 180 + 3
#     lamda0 = lamda0*math.pi/180.0
    
#     phi = lat*math.pi/180.0
#     lamda = lon*math.pi/180.0

#     v = 1/math.sqrt(1 - e2*(math.sin(phi)*math.sin(phi)))
#     A = (lamda - lamda0)*math.cos(phi)
#     T = math.tan(phi)*math.tan(phi)
#     C = e2*math.cos(phi)*math.cos(phi)/(1-e2)
#     s = (1-e2/4 - 3*e2*e2/64 - 5*e2*e2*e2/256)*phi - (3*e2/8+3*e2*e2/32+45*e2*e2*e2/1024)*math.sin(2*phi)
#     +(15*e2*e2/256+45*e2*e2*e2/1024)*math.sin(4*phi) - 35*e2*e2*e2/3072*math.sin(6*phi)
#     UTME = (E0 + k0*a*v*(A + (1-T+C)*A*A*A/6 + (5-18*T+T*T)*A*A*A*A*A/120))*1000.0
#     UTMN = (N0 + k0*a*(s+v*math.tan(phi)*(A*A/2 + (5-T+9*C+4*C*C)*A*A*A*A/24+(61-58*T+T*T)*A*A*A*A*A*A/720)))*1000.0
#     #UTME = E0 + k0*a*v*(A + (1-T+C)*A*A*A/6 + (5-18*T+T*T)*A*A*A*A*A/120)
#     #UTMN = N0 + k0*a*(s+v*math.tan(phi)*(A*A/2 + (5-T+9*C+4*C*C)*A*A*A*A/24+(61-58*T+T*T)*A*A*A*A*A*A/720))
#     return UTME,UTMN


def lonlat_to_utm(lat, lon):
    deg2rad = math.pi / 180.0
    rad2deg = 180.0 / math.pi

    zone_id = int(lon/6) + 31
    # WGS-84 reference system parameters
    earth_radius = 6378137
    ecc_squared  = 0.00669438
    k0           = 0.9996


    long_temp = (lon + 180) - (int)((lon + 180) / 360) * 360 - 180 # -180.00 .. 179.9
    lat_rad   = lat * deg2rad
    long_rad  = long_temp * deg2rad

    long_origin    = zone_id * 6 - 183  #*+3 puts origin in middle of zone
    long_originRad = long_origin * deg2rad

    ecc_prime_squared = (ecc_squared)/(1 - ecc_squared)

    n = earth_radius / math.sqrt(1 - ecc_squared * math.sin(lat_rad) * math.sin(lat_rad))
    t = math.tan(lat_rad) * math.tan(lat_rad)
    c = ecc_prime_squared * math.cos(lat_rad) * math.cos(lat_rad)
    a = math.cos(lat_rad) * (long_rad - long_originRad)

    m = earth_radius * ((1 - ecc_squared / 4 - 3 * ecc_squared * ecc_squared / 64 -
                         5 * ecc_squared * ecc_squared * ecc_squared / 256) *
                            lat_rad -
                        (3 * ecc_squared / 8 + 3 * ecc_squared * ecc_squared / 32 +
                         45 * ecc_squared * ecc_squared * ecc_squared / 1024) *
                            math.sin(2 * lat_rad) +
                        (15 * ecc_squared * ecc_squared / 256 + 45 * ecc_squared * ecc_squared * ecc_squared / 1024) *
                            math.sin(4 * lat_rad) -
                        (35 * ecc_squared * ecc_squared * ecc_squared / 3072) * math.sin(6 * lat_rad))

    easting = k0 * n *(a + (1 - t + c) * a * a * a / 6 +(5 - 18 * t + t * t + 72 * c - 58 * ecc_prime_squared) * a * a * a * a * a / 120) + 500000.0
    northing = k0 * (m + n * math.tan(lat_rad) *(a * a / 2 + (5 - t + 9 * c + 4 * c * c) * a * a * a * a / 24 +
                       (61 - 58 * t + t * t + 600 * c - 330 * ecc_prime_squared) * a * a * a * a * a * a / 720))
    northing += 10000000.0  # 10000000 meter offset for southern hemisphere
    return easting,northing

# retcode_t utm_to_lonlat(uint8_t zone_id, bool_t south_flag, float64_t easting, float64_t northing, float64_t* lon,
#                         float64_t* lat)
# {
#     retcode_t rc = RC_SUCCESS;
#     float64_t ecc_prime_squared;
#     float64_t e1;
#     float64_t n1, t1, c1, r1, d, m;
#     float64_t long_origin;
#     float64_t mu, phi1_rad;
#     float64_t x, y;

#     assert(lat != NULL);
#     assert(lon != NULL);
#     assert(isnan(northing) == 0);
#     assert(isnan(easting) == 0);

#     e1 = (1 - sqrt(1 - ecc_squared)) / (1 + sqrt(1 - ecc_squared));

#     x = easting - 500000.0;  // remove 500,000 meter offset for longitude
#     y = northing;
#     if (south_flag)
#     {
#         y -= 10000000.0;
#     }

#     long_origin = (zone_id - 1) * 6 - 180 + 3;  // +3 puts origin in middle of zone

#     ecc_prime_squared = (ecc_squared) / (1 - ecc_squared);

#     m  = y / k0;
#     mu = m / (earth_radius * (1 - ecc_squared / 4 - 3 * ecc_squared * ecc_squared / 64 -
#                               5 * ecc_squared * ecc_squared * ecc_squared / 256));

#     phi1_rad = mu + (3 * e1 / 2 - 27 * e1 * e1 * e1 / 32) * sin(2 * mu) +
#                (21 * e1 * e1 / 16 - 55 * e1 * e1 * e1 * e1 / 32) * sin(4 * mu) +
#                (151 * e1 * e1 * e1 / 96) * sin(6 * mu);

#     n1 = earth_radius / sqrt(1 - ecc_squared * sin(phi1_rad) * sin(phi1_rad));
#     t1 = tan(phi1_rad) * tan(phi1_rad);
#     c1 = ecc_prime_squared * cos(phi1_rad) * cos(phi1_rad);
#     r1 = earth_radius * (1 - ecc_squared) / pow(1 - ecc_squared * sin(phi1_rad) * sin(phi1_rad), 1.5);
#     d  = x / (n1 * k0);

#     *lat =
#         phi1_rad - (n1 * tan(phi1_rad) / r1) *
#                        (d * d / 2 - (5 + 3 * t1 + 10 * c1 - 4 * c1 * c1 - 9 * ecc_prime_squared) * d * d * d * d / 24 +
#                         (61 + 90 * t1 + 298 * c1 + 45 * t1 * t1 - 252 * ecc_prime_squared - 3 * c1 * c1) * d * d * d *
#                             d * d * d / 720);
#     *lat = *lat * rad2deg;

#     *lon = (d - (1 + 2 * t1 + c1) * d * d * d / 6 +
#             (5 - 2 * c1 + 28 * t1 - 3 * c1 * c1 + 8 * ecc_prime_squared + 24 * t1 * t1) * d * d * d * d * d / 120) /
#            cos(phi1_rad);
#     *lon = long_origin + *lon * rad2deg;

#     if (isnan(*lat) || isnan(*lon))
#     {
#         rc = RC_FAIL;
#     }

#     return rc;



