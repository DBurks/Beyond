from alarm import Alarm
from sensor import Sensor
from unittest.mock import Mock
import pytest

@pytest.fixture()
def stub_low_sensor():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 15
    return stub_sensor

@pytest.fixture()
def stub_high_sensor():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 22
    return stub_sensor

@pytest.fixture()
def stub_normal_sensor():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    return stub_sensor

## Checking the default sensor is not testable
def test_alarm_is_off_by_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on

## So we use the stubbed sensor in the fixtures above
def test_low_pressure_activates_alarm(stub_low_sensor):
    alarm = Alarm(stub_low_sensor)
    alarm.check()
    assert alarm.is_alarm_on

def test_high_pressure_activates_alarm(stub_high_sensor):
    alarm = Alarm(stub_high_sensor)
    alarm.check()
    assert alarm.is_alarm_on

def test_normal_pressure_alarm_stays_off(stub_normal_sensor):
    alarm = Alarm(stub_normal_sensor)
    alarm.check()
    assert not alarm.is_alarm_on
