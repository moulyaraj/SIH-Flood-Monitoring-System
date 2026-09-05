
#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>

typedef struct struct_message {
    char nodeId[16];
    float distance;
    float temperature;
    int rain;
    float vibration;
} struct_message;

struct_message incomingReadings;

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
    memcpy(&incomingReadings, incomingData, sizeof(incomingReadings));
    
    // Transmit JSON over Serial to Python
    Serial.printf("{\"node\":\"%s\",\"dist\":%.1f,\"temp\":%.1f,\"rain\":%d,\"vib\":%.2f}\n",
                  incomingReadings.nodeId,
                  incomingReadings.distance,
                  incomingReadings.temperature,
                  incomingReadings.rain,
                  incomingReadings.vibration);
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);

    if (esp_now_init() != ESP_OK) {
        Serial.println("ESP-NOW Init Failed");
        return;
    }

    esp_now_register_recv_cb((esp_now_recv_cb_t)OnDataRecv);
}

void loop() {
    vTaskDelay(1000 / portTICK_PERIOD_MS);
}
