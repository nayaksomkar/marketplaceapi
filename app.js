const API_BASE = 'http://localhost:5000';

const endpoints = [
    { name: 'customers', table: 'customers-table' },
    { name: 'sellers', table: 'sellers-table' },
    { name: 'items', table: 'items-table' },
    { name: 'deliveries', table: 'deliveries-table' }
];

async function fetchData(endpoint, tableId) {
    const table = document.getElementById(tableId);
    const tbody = table.querySelector('tbody');
    
    try {
        const response = await fetch(`${API_BASE}/api/${endpoint}`);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        
        const data = await response.json();
        
        tbody.innerHTML = '';
        
        if (!Array.isArray(data) || data.length === 0) {
            tbody.innerHTML = '<tr><td colspan="3" class="loading">No data available</td></tr>';
            return;
        }
        
        data.forEach(item => {
            const row = document.createElement('tr');
            
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
                row.innerHTML = `
                    <td>${item.name || '-'}</td>
                    <td>${item.email || '-'}</td>
                    <td>${item.address || '-'}</td>
                `;
            }
            
            tbody.appendChild(row);
        });
        
    } catch (error) {
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

function formatLocation(location) {
    if (!location) return '-';
    if (typeof location === 'object') {
        return `${location.lat || ''}, ${location.lon || ''}`;
    }
    return location;
}

function init() {
    endpoints.forEach(({ name, table }) => {
        fetchData(name, table);
    });
}

document.addEventListener('DOMContentLoaded', init);
