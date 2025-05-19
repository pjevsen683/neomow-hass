class NeomowMapCard extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    setConfig(config) {
        this.config = config;
        this.render();
    }

    render() {
        if (!this.config || !this.config.entity) {
            this.shadowRoot.innerHTML = '<div>Error: Entity not configured</div>';
            return;
        }

        this.shadowRoot.innerHTML = `
            <ha-card>
                <div class="card-content">
                    <div id="map-container"></div>
                </div>
            </ha-card>
            <style>
                ha-card {
                    padding: 16px;
                }
                #map-container {
                    width: 100%;
                    height: 300px;
                    background-color: #f3f4f6;
                    border-radius: 4px;
                    overflow: hidden;
                }
                #map-container svg {
                    width: 100%;
                    height: 100%;
                }
            </style>
        `;

        this.mapContainer = this.shadowRoot.getElementById('map-container');
    }

    set hass(hass) {
        if (!this.config || !this.config.entity) return;

        const entity = hass.states[this.config.entity];
        if (!entity) return;

        if (entity.state) {
            this.mapContainer.innerHTML = entity.state;
        }
    }

    getCardSize() {
        return 3;
    }
}

customElements.define('neomow-map-card', NeomowMapCard); 