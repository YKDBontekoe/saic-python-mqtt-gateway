AVAILABLE = 'available'

CLIMATE = 'climate'
CLIMATE_BACK_WINDOW_HEAT = CLIMATE + '/rearWindowDefrosterHeating'
CLIMATE_FRONT_WINDOW_HEAT = CLIMATE + '/frontWindowDefrosterHeating'
CLIMATE_EXTERIOR_TEMPERATURE = CLIMATE + '/exteriorTemperature'
CLIMATE_INTERIOR_TEMPERATURE = CLIMATE + '/interiorTemperature'
CLIMATE_REMOTE_CLIMATE_STATE = CLIMATE + '/remoteClimateState'
CLIMATE_REMOTE_TEMPERATURE = CLIMATE + '/remoteTemperature'
CLIMATE_HEATED_SEATS_FRONT_LEFT_LEVEL = CLIMATE + '/heatedSeatsFrontLeftLevel'
CLIMATE_HEATED_SEATS_FRONT_RIGHT_LEVEL = CLIMATE + '/heatedSeatsFrontRightLevel'

WINDOWS = 'windows'
WINDOWS_DRIVER = WINDOWS + '/driver'
WINDOWS_PASSENGER = WINDOWS + '/passenger'
WINDOWS_REAR_LEFT = WINDOWS + '/rearLeft'
WINDOWS_REAR_RIGHT = WINDOWS + '/rearRight'
WINDOWS_SUN_ROOF = WINDOWS + '/sunRoof'

DOORS = 'doors'
DOORS_BONNET = DOORS + '/bonnet'
DOORS_BOOT = DOORS + '/boot'
DOORS_DRIVER = DOORS + '/driver'
DOORS_LOCKED = DOORS + '/locked'
DOORS_PASSENGER = DOORS + '/passenger'
DOORS_REAR_LEFT = DOORS + '/rearLeft'
DOORS_REAR_RIGHT = DOORS + '/rearRight'

LIGHTS = 'lights'
LIGHTS_MAIN_BEAM = LIGHTS + '/mainBeam'
LIGHTS_DIPPED_BEAM = LIGHTS + '/dippedBeam'

DRIVETRAIN = 'drivetrain'
DRIVETRAIN_AUXILIARY_BATTERY_VOLTAGE = DRIVETRAIN + '/auxiliaryBatteryVoltage'
DRIVETRAIN_CHARGER_CONNECTED = DRIVETRAIN + '/chargerConnected'
DRIVETRAIN_CHARGING = DRIVETRAIN + '/charging'
DRIVETRAIN_BATTERY_HEATING = DRIVETRAIN + '/batteryHeating'
DRIVETRAIN_CHARGING_SCHEDULE = DRIVETRAIN + '/chargingSchedule'
DRIVETRAIN_BATTERY_HEATING_SCHEDULE = DRIVETRAIN + '/batteryHeatingSchedule'
DRIVETRAIN_CHARGING_TYPE = DRIVETRAIN + '/chargingType'
DRIVETRAIN_CURRENT = DRIVETRAIN + '/current'
DRIVETRAIN_HV_BATTERY_ACTIVE = DRIVETRAIN + '/hvBatteryActive'
DRIVETRAIN_MILEAGE = DRIVETRAIN + '/mileage'
DRIVETRAIN_MILEAGE_OF_DAY = DRIVETRAIN + '/mileageOfTheDay'
DRIVETRAIN_MILEAGE_SINCE_LAST_CHARGE = DRIVETRAIN + '/mileageSinceLastCharge'
DRIVETRAIN_POWER = DRIVETRAIN + '/power'
DRIVETRAIN_POWER_USAGE_OF_DAY = DRIVETRAIN + '/powerUsageOfDay'
DRIVETRAIN_POWER_USAGE_SINCE_LAST_CHARGE = DRIVETRAIN + '/powerUsageSinceLastCharge'
DRIVETRAIN_RANGE = DRIVETRAIN + '/range'
DRIVETRAIN_RUNNING = DRIVETRAIN + '/running'
DRIVETRAIN_REMAINING_CHARGING_TIME = DRIVETRAIN + '/remainingChargingTime'
DRIVETRAIN_HYBRID_ELECTRICAL_RANGE = DRIVETRAIN + '/hybrid_electrical_range'
DRIVETRAIN_SOC = DRIVETRAIN + '/soc'
DRIVETRAIN_SOC_TARGET = DRIVETRAIN + '/socTarget'
DRIVETRAIN_CHARGECURRENT_LIMIT = DRIVETRAIN + '/chargeCurrentLimit'
DRIVETRAIN_SOC_KWH = DRIVETRAIN + '/soc_kwh'
DRIVETRAIN_LAST_CHARGE_ENDING_POWER = DRIVETRAIN + '/lastChargeEndingPower'
DRIVETRAIN_TOTAL_BATTERY_CAPACITY = DRIVETRAIN + '/totalBatteryCapacity'
DRIVETRAIN_VOLTAGE = DRIVETRAIN + '/voltage'
DRIVETRAIN_CHARGING_CABLE_LOCK = DRIVETRAIN + '/chargingCableLock'

INFO = 'info'
INFO_BRAND = INFO + '/brand'
INFO_MODEL = INFO + '/model'
INFO_YEAR = INFO + '/year'
INFO_SERIES = INFO + '/series'
INFO_COLOR = INFO + '/color'
INFO_CONFIGURATION = INFO + '/configuration'
INFO_LAST_MESSAGE = INFO + '/lastMessage'
INFO_LAST_MESSAGE_ID = INFO_LAST_MESSAGE + '/messageId'
INFO_LAST_MESSAGE_TYPE = INFO_LAST_MESSAGE + '/messageType'
INFO_LAST_MESSAGE_TITLE = INFO_LAST_MESSAGE + '/title'
INFO_LAST_MESSAGE_TIME = INFO_LAST_MESSAGE + '/messageTime'
INFO_LAST_MESSAGE_SENDER = INFO_LAST_MESSAGE + '/sender'
INFO_LAST_MESSAGE_CONTENT = INFO_LAST_MESSAGE + '/content'
INFO_LAST_MESSAGE_STATUS = INFO_LAST_MESSAGE + '/status'
INFO_LAST_MESSAGE_VIN = INFO_LAST_MESSAGE + '/vin'

INTERNAL = '_internal'
INTERNAL_API = INTERNAL + '/api'
INTERNAL_LWT = INTERNAL + '/lwt'
INTERNAL_ABRP = INTERNAL + '/abrp'
INTERNAL_CONFIGURATION_RAW = INTERNAL + '/configuration/raw'

LOCATION = 'location'
LOCATION_POSITION = LOCATION + '/position'
LOCATION_HEADING = LOCATION + '/heading'
LOCATION_LATITUDE = LOCATION + '/latitude'
LOCATION_LONGITUDE = LOCATION + '/longitude'
LOCATION_SPEED = LOCATION + '/speed'
LOCATION_ELEVATION = LOCATION + '/elevation'

REFRESH = 'refresh'
REFRESH_LAST_ACTIVITY = REFRESH + '/lastActivity'
REFRESH_LAST_CHARGE_STATE = REFRESH + '/lastChargeState'
REFRESH_LAST_VEHICLE_STATE = REFRESH + '/lastVehicleState'
REFRESH_MODE = REFRESH + '/mode'
REFRESH_PERIOD = REFRESH + '/period'
REFRESH_PERIOD_ACTIVE = REFRESH_PERIOD + '/active'
REFRESH_PERIOD_CHARGING = REFRESH_PERIOD + '/charging'
REFRESH_PERIOD_INACTIVE = REFRESH_PERIOD + '/inActive'
REFRESH_PERIOD_AFTER_SHUTDOWN = REFRESH_PERIOD + '/afterShutdown'
REFRESH_PERIOD_INACTIVE_GRACE = REFRESH_PERIOD + '/inActiveGrace'

TYRES = 'tyres'
TYRES_FRONT_LEFT_PRESSURE = TYRES + '/frontLeftPressure'
TYRES_FRONT_RIGHT_PRESSURE = TYRES + '/frontRightPressure'
TYRES_REAR_LEFT_PRESSURE = TYRES + '/rearLeftPressure'
TYRES_REAR_RIGHT_PRESSURE = TYRES + '/rearRightPressure'

VEHICLES = 'vehicles'
