// {}
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z} from "zod/v4";

// Create an MCP server
const server = new McpServer({
  name: "cv-ocr",
  version: "1.0.0"
});

server.tool(
    'get-cv',
    'Tool to get data cv',
    {
        cv_content: z.string().describe('content oncv')
    },
    async ({ cv_content }) => {
        return {
            content: [
                {
                    type: "text",
                    text: `Received CV content of length ${cv_content}`,
                }
            ]
        }
    }
);

const transport = new StdioServerTransport();
server.connect(transport);