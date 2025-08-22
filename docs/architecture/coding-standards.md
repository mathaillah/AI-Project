## Coding Standards

These standards are MANDATORY for AI agents.

### Core Standards

-   **Languages & Runtimes:** TypeScript 5.x, Node.js 20.x
-   **Style & Linting:** ESLint with Prettier
-   **Test Organization:** Tests co-located with source files (e.g., `user.service.ts`, `user.service.spec.ts`)

### Naming Conventions

| Element | Convention | Example |
|---|---|---|
| **Variables** | camelCase | `userName` |
| **Functions** | camelCase | `getUserById` |
| **Classes** | PascalCase | `UserService` |
| **Files** | kebab-case | `user-service.ts` |

### Critical Rules

-   **Logging:** Never use `console.log` in production code; use the configured logger.
-   **API Responses:** All API responses must use a standardized `ApiResponse` wrapper type.
-   **Database Access:** Database queries must use the repository pattern; never direct ORM calls in controllers/services.
