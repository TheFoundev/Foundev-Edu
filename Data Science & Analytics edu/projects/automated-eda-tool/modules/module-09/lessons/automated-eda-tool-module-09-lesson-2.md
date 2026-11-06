# Read auth and contact in the source

**Lesson ID:** `automated-eda-tool-module-09-lesson-2`

## Purpose and learning objectives

Study the implementation in [frontend/src/components/Auth.jsx] and [frontend/src/components/Contact.jsx]. Trace its declarations and dependencies into a caller or test. Inspect imports, declarations, and call sites in the file; filenames alone do not establish its role.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `frontend/src/components/Auth.jsx`, `frontend/src/components/Contact.jsx`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `frontend/src/components/Auth.jsx`, `import { useState } from 'react';` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `frontend/src/components/Auth.jsx`, `import { Card, CardContent } from "@/components/ui/card";` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `frontend/src/components/Auth.jsx`, `import { Button } from "@/components/ui/button";` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `frontend/src/components/Auth.jsx`, `import { Input } from "@/components/ui/input";` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `frontend/src/components/Auth.jsx`, `import { useForm } from "react-hook-form";` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `frontend/src/components/Contact.jsx`, `import React, { useState } from "react";` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `frontend/src/components/Contact.jsx`, `import { motion } from "framer-motion";` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### frontend/src/components/Auth.jsx

```text
import { useState } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useForm } from "react-hook-form";
import { motion, AnimatePresence } from "framer-motion";
import { useNavigate } from 'react-router-dom';
import { Loader2, Eye, EyeOff, AlertCircle } from 'lucide-react';
import { toast } from 'sonner';
import { useAuth0 } from "@auth0/auth0-react";


const AuthForm = ({ isLogin, toggleForm }) => {
  const {user, loginWithRedirect, isAuthenticated, logout} = useAuth0();
  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
    setError,
    clearErrors,
  } = useForm();

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [authError, setAuthError] = useState(null);
  const navigate = useNavigate();
  const password = watch('password');

  const passwordStrength = () => {
    if (!password) return 0;
    let strength = 0;
    if (password.length >= 8) strength += 1;
    if (/[A-Z]/.test(password)) strength += 1;
    if (/[0-9]/.test(password)) strength += 1;
    if (/[^A-Za-z0-9]/.test(password)) strength += 1;
    return strength;
  };

  const onSubmit = async (data) => {
    setIsSubmitting(true);
    setAuthError(null);
    clearErrors('root');
    
    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:5000';
      const endpoint = isLogin ? '/login' : '/signup';
      
      const response = await fetch(`${apiUrl}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: data.email,
          password: data.password,
          ...(isLogin ? {} : { name: data.name })
        }),
        credentials: 'include'
      });
      
      const result = await response.json();
      
      if (!response.ok) {
        setAuthError(result.message || 'Authentication failed. Please try again.');
        return;
      }
      if (result.token) {
        localStorage.setItem('authToken', result.token);
      }
      
      if (result.user) {
        localStorage.setItem('user', JSON.stringify(result.user));
      }
      
      toast.success(result.message || (isLogin ? 'Login successful!' : 'Account created successfully!'));
      
      navigate('/');
      
    } catch (error) {
      console.error('Authentication error:', error);
      setAuthError('An unexpected error occurred. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {authError && (
        <div className="p-3 rounded-md bg-red-50 border border-red-200 flex items-start gap-2">
          <AlertCircle className="h-5 w-5 text-red-500 mt-0.5 flex-shrink-0" />
          <p className="text-sm text-red-600">{authError}</p>
        </div>
      )}
      
      {!isLogin && (
        <div className="space-y-1.5">
          <Input 
            placeholder="Full name" 
```

### frontend/src/components/Contact.jsx

```text
import React, { useState } from "react";
import { motion } from "framer-motion";

const Contact = () => {
    const [submitted, setSubmitted] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        setSubmitted(true);
    };

    return (
        <motion.div
            className="container mx-auto px-4 py-16 max-w-2xl"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
        >
            <h2 className="text-3xl font-bold text-center mb-4 text-emerald-600 dark:text-emerald-400">Leave a Review</h2>
            <p className="text-gray-600 dark:text-slate-400 text-center mb-6">
                We value your feedback! Share your experience with AutoEDA.
            </p>

            {submitted ? (
                <div className="p-4 bg-emerald-100 dark:bg-emerald-700 text-emerald-800 dark:text-white rounded-xl text-center shadow-lg">
                    Message submitted successfully! Thank you for reaching out.
                </div>
            ) : (
                <form onSubmit={handleSubmit} className="space-y-6 bg-white dark:bg-[#111827] p-6 rounded-xl shadow-xl">
                    <div>
                        <label className="block text-gray-700 dark:text-gray-200 mb-2 font-medium">Name</label>
                        <input
                            type="text"
                            placeholder="Your name"
                            required
                            className="w-full p-3 border border-gray-300 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-gray-900 dark:text-gray-50 bg-white dark:bg-slate-800 placeholder-gray-400 dark:placeholder-slate-400"
                        />
                    </div>

                    <div>
                        <label className="block text-gray-700 dark:text-gray-200 mb-2 font-medium">Email</label>
                        <input
                            type="email"
                            placeholder="Your email"
                            required
                            className="w-full p-3 border border-gray-300 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-gray-900 dark:text-gray-50 bg-white dark:bg-slate-800 placeholder-gray-400 dark:placeholder-slate-400"
                        />
                    </div>

                    <div>
                        <label className="block text-gray-700 dark:text-gray-200 mb-2 font-medium">Type</label>
                        <select
                            required
                            className="w-full p-3 border border-gray-300 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-gray-900 dark:text-gray-50 bg-white dark:bg-slate-800 placeholder-gray-400 dark:placeholder-slate-400"
                        >
                            <option value="" disabled selected>Select an option</option>
                            <option value="Feedback">Feedback</option>
                            <option value="Bug Report">Bug Report</option>
                            <option value="Feature Request">Feature Request</option>
                        </select>
                    </div>

                    <div>
                        <label className="block text-gray-700 dark:text-gray-200 mb-2 font-medium">Message</label>
                        <textarea
                            placeholder="Your message..."
                            required
                            rows={4}
                            className="w-full p-3 border border-gray-300 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-gray-900 dark:text-gray-50 bg-white dark:bg-slate-800 placeholder-gray-400 dark:placeholder-slate-400"
                        ></textarea>
                    </div>

                    <button

```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change.

## Summary

This lesson ties its explanation to `frontend/src/components/Auth.jsx`, `frontend/src/components/Contact.jsx`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
