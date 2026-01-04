// types.ts
export interface User {
  id: string;
  username: string;
  email: string;
  password: string;
  role: 'admin' | 'moderator' | 'user';
}

export interface AuthToken {
  token: string;
  expiresAt: number;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
}

export interface ErrorResponse {
  message: string;
  statusCode: number;
}

export interface AuthResponse {
  user: User;
  token: AuthToken;
}