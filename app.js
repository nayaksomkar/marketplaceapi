/* =============================================
   Marketplace Dashboard JavaScript
   ============================================= */

// API base URL - change if API runs on different port
const API_BASE = 'http://localhost:5000';

// Endpoints to fetch with their table IDs
const endpoints = [
    { name: 'customers', table: 'customers-table' },
    { name: 'sellers', table: 'sellers-table' },
    { name: 'items', table: 'items-table' },
    { name: 'deliveries', table: 'deliveries-table' }
];

/* =============================================
   Data Fetching Functions
   ============================================= */

/**
 * Fetch data from API and populate table
 * @param {string} endpoint - API endpoint name (e.g., 'customers')
 * @param {string} tableId - HTML table ID to populate
 */
async function fetchData(endpoint, tableId) {
    const table = document.getElementById(tableId);
    const tbody = table.querySelector('tbody');
    
    try {
        // Fetch data from API
        const response = await fetch(`${API_BASE}/api/${endpoint}`);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        
        const data = await response.json();
        
        // Clear existing table content
        tbody.innerHTML = '';
        
        // Handle empty data
        if (!Array.isArray(data) || data.length === 0) {
            tbody.innerHTML = '<tr><td colspan="3" class="loading">No data available</td></tr>';
            return;
        }
        
        // Populate table with data
        data.forEach(item => {
            const row = document.createElement('tr');
            
            // Format row based on endpoint type
            if (endpoint === 'deliveries') {
                row.innerHTML = `
                    <td>${item.order_id || '-'}</td>
                    <td>${item.status || '-'}</td>
                    <td>${formatLocation(item.location)}</td>
                `;
            } else if (endpoint === 'items') {
                row.innerHTML = `
                    <td>${item.name || '-'}</td>
                    <td>${item.description || '-'}</td>
                    <td>$${(item.price || 0).toFixed(2)}</td>
                `;
            } else if (endpoint === 'sellers') {
                row.innerHTML = `
                    <td>${item.name || '-'}</td>
                    <td>${item.email || '-'}</td>
                    <td>${item.business_name || '-'}</td>
                `;
            } else {
                // Customers
                row.innerHTML = `
                    <td>${item.name || '-'}</td>
                    <td>${item.email || '-'}</td>
                    <td>${item.address || '-'}</td>
                `;
            }
            
            tbody.appendChild(row);
        });
        
    } catch (error) {
        // Show error message on failure
        console.error(`Error loading ${endpoint}:`, error);
        tbody.innerHTML = `
            <tr>
                <td colspan="3" class="error">
                    Failed to load data. Make sure the API is running.
                </td>
            </tr>
        `;
    }
}

/**
 * Format location object to display string
 * @param {object} location - Location object with lat/lon
 * @returns {string} Formatted location string
 */
function formatLocation(location) {
    if (!location) return '-';
    if (typeof location === 'object') {
        return `${location.lat || ''}, ${location.lon || ''}`;
    }
    return location;
}

/* =============================================
   Initialization
   ============================================= */

/**
 * Initialize dashboard by fetching all endpoint data
 */
function init() {
    endpoints.forEach(({ name, table }) => {
        fetchData(name, table);
    });
}

// Start initialization when DOM is ready
document.addEventListener('DOMContentLoaded', init);
