import React, { useState, useEffect } from 'react';
import axios from 'axios';

const LoanApplications = () => {
    const [loanApplications, setLoanApplications] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/loan-applications')
            .then(response => {
                setLoanApplications(response.data);
            })
            .catch(error => {
                console.error('Error fetching loan applications: ', error);
            });
    }, []);

    return (
        <div>
            <h2>Loan Applications</h2>
            <ul>
                {loanApplications.map(application => (
                    <li key={application.id}>
                        <strong>{application.business_name}</strong> - {application.loan_amount} - {application.purpose}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default LoanApplications;
