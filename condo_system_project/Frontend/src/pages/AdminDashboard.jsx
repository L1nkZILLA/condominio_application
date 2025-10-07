import React from 'react';

export default function AdminDashboard(){
  return (
    <div style={{padding:20}}>
      <h1>Admin Dashboard</h1>
      <nav>
        <ul>
          <li>Usuarios</li>
          <li>Permissoes</li>
          <li>Grupos / Empresas</li>
          <li>Unidades</li>
          <li>Reservas</li>
          <li>Visitantes</li>
          <li>Manutenção</li>
          <li>Avisos</li>
          <li>Logs / Auditoria</li>
        </ul>
      </nav>
      <section>
        <h2>Visão Geral</h2>
        <p>Conteúdo de dashboard ...</p>
      </section>
    </div>
  );
}
